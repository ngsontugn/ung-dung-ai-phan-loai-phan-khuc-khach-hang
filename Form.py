import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from Process import process
import datetime

with open("model_kmeans.pkl", "rb") as model_file:
    model = pickle.load(model_file)
with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)
with open("cluster_labels.pkl", "rb") as label_file:
    cluster_labels = pickle.load(label_file)

st.title("Dự đoán phân cụm khách hàng dựa trên RFM")

option = st.radio("Chọn phương thức nhập dữ liệu:", ("Nhập thủ công", "Tải file CSV"))

if option == "Nhập thủ công":
    purchase_date = st.date_input("Ngày mua hàng gần nhất:", max_value=datetime.date.today())
    frequency = st.number_input("Frequency (số lần mua hàng):", min_value=0, step=1)
    monetary = st.number_input("Monetary (tổng chi tiêu):", min_value=0.0, step=0.1)

    today = datetime.date.today()
    recency = (today - purchase_date).days

    if st.button("Dự đoán"):
        input_data = np.array([[recency, frequency, monetary]])
        input_scaled = scaler.transform(input_data)

        cluster_index = model.predict(input_scaled)[0]
        cluster_label = cluster_labels[cluster_index]
        st.success(f"Khách hàng thuộc nhóm: {cluster_label}")
else:
    uploaded_file = st.file_uploader("Tải lên file CSV chứa dữ liệu RFM", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding='latin-1')
        df = process(df)
        df_process = df.drop(columns=['CustomerID'])
        input_scaled = scaler.transform(df_process)
        df["Cluster"] = model.predict(input_scaled)

        df["Cluster"] = df["Cluster"].apply(lambda x: cluster_labels[x])

        st.write("Dự đoán phân cụm:")
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(label="Tải xuống kết quả", data=csv, file_name="predicted_clusters.csv", mime="text/csv")

