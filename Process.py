import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def process(data):
    # remove error
    data = data.dropna(subset=['CustomerID', 'Description'])
    data.drop_duplicates(inplace=True)

    data['Transaction_Status'] = np.where(data['InvoiceNo'].astype(str).str.startswith('C'), 'Cancelled', 'Completed')
    data.loc[data['Quantity'] < 0, 'Quantity'] = 0
    data = data[data['Transaction_Status'] == 'Completed']

    unique_stock_codes = data['StockCode'].unique()
    numeric_char_counts_in_unique_codes = pd.Series(unique_stock_codes).apply(lambda x: sum(c.isdigit() for c in str(x))).value_counts()
    anomalous_stock_codes = [code for code in unique_stock_codes if sum(c.isdigit() for c in str(code)) in (0, 1)]
    data = data[~data['StockCode'].isin(anomalous_stock_codes)]
    
    data = data[data['UnitPrice'] > 0]

    # RFM
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data['InvoiceDay'] = data['InvoiceDate'].dt.date
    customer_data = data.groupby('CustomerID')['InvoiceDay'].max().reset_index()
    most_recent_date = data['InvoiceDay'].max()
    customer_data['InvoiceDay'] = pd.to_datetime(customer_data['InvoiceDay'])
    most_recent_date = pd.to_datetime(most_recent_date)
    customer_data['Recency'] = (most_recent_date - customer_data['InvoiceDay']).dt.days
    customer_data.drop(columns=['InvoiceDay'], inplace=True)

    total_transactions = data.groupby('CustomerID')['InvoiceNo'].nunique().reset_index()
    total_transactions.rename(columns={'InvoiceNo': 'Frequency'}, inplace=True)
    customer_data = pd.merge(customer_data, total_transactions, on='CustomerID')

    data['Monetary'] = data['UnitPrice'] * data['Quantity']
    total_spend = data.groupby('CustomerID')['Monetary'].sum().reset_index()
    customer_data = pd.merge(customer_data, total_spend, on='CustomerID')

    # remove outliers
    model = IsolationForest(contamination=0.05, random_state=0)
    customer_data['Outlier_Scores'] = model.fit_predict(customer_data.iloc[:, 1:].to_numpy())
    customer_data['Is_Outlier'] = [1 if x == -1 else 0 for x in customer_data['Outlier_Scores']]
    outliers_data = customer_data[customer_data['Is_Outlier'] == 1]
    customer_data_cleaned = customer_data[customer_data['Is_Outlier'] == 0]
    customer_data_cleaned = customer_data_cleaned.drop(columns=['Outlier_Scores', 'Is_Outlier'])
    customer_data_cleaned.reset_index(drop=True, inplace=True)

    return customer_data_cleaned