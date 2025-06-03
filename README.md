# 🤖 Ứng dụng AI phân loại phân khúc khách hàng trong bán lẻ trực tuyến

> **Môn học:** Ứng dụng trí tuệ nhân tạo trong quản lý và kinh doanh\
> **Thời gian thực hiện:** 01/2025 - 05/2025
> **Liên hệ:** ngsontugn@gmail.com | [LinkedIn](https://linkedin.com/in/ngsontugn)

---

## 📌 Mô tả dự án

Dự án ứng dụng thuật toán **K-means clustering** để phân nhóm khách hàng trong lĩnh vực **bán lẻ trực tuyến**, dựa trên dữ liệu thực tế từ kho dữ liệu **UCI (Online Retail Dataset)**.

Thông qua việc phân tích các chỉ số RFM (Recency - Frequency - Monetary), hệ thống giúp doanh nghiệp:

- Xác định nhóm khách hàng trung thành, tiềm năng và có nguy cơ rời bỏ
- Tối ưu hóa chiến dịch marketing và chăm sóc khách hàng
- Tăng hiệu quả chuyển đổi và giảm chi phí tiếp thị

---

## 🎯 Mục tiêu

- Xây dựng mô hình AI tự động phân cụm khách hàng theo đặc điểm hành vi mua sắm
- Áp dụng chuẩn hóa dữ liệu và đánh giá hiệu quả mô hình bằng các chỉ số thống kê
- Triển khai giao diện đầu vào/đầu ra hỗ trợ sử dụng mô hình cho nhân viên kinh doanh/marketing

---

## 📂 Dữ liệu sử dụng

- **Nguồn:** Dataset "Online Retail" từ UCI Machine Learning Repository  
- **Dung lượng:** ~540,000 dòng dữ liệu, từ 38 quốc gia, chủ yếu tại Anh  
- **Định dạng:** CSV, gồm các trường như `CustomerID`, `InvoiceDate`, `Quantity`, `UnitPrice`, `Country`...

---

## 🔧 Các bước thực hiện

1. **Tiền xử lý dữ liệu**
   - Loại bỏ giao dịch hủy (`InvoiceNo` bắt đầu bằng "C")
   - Xử lý missing values
   - Phát hiện và loại outliers bằng Isolation Forest

2. **Tạo đặc trưng RFM**
   - Recency: Số ngày kể từ lần mua gần nhất
   - Frequency: Tần suất mua hàng
   - Monetary: Tổng chi tiêu

3. **Chuẩn hóa dữ liệu**
   - Dùng `StandardScaler` để chuẩn hóa dữ liệu đầu vào

4. **Phân cụm với KMeans**
   - Sử dụng phương pháp Elbow để xác định số cụm `k`
   - Chạy mô hình KMeans với `k=3`

5. **Đánh giá mô hình**
   - Chỉ số Silhouette: `0.484` (tốt)
   - Davies-Bouldin: `0.728` (càng thấp càng tốt)
   - Calinski-Harabasz: `4576` (càng cao càng tốt)

6. **Triển khai giao diện người dùng**
   - Nhập liệu thủ công (1 khách hàng)
   - Upload file CSV (nhiều khách hàng)
   - Xuất kết quả bảng phân cụm khách hàng

---

## 🧠 Kết quả phân cụm

| Cụm | Recency | Frequency | Monetary | Diễn giải |
|-----|---------|-----------|----------|-----------|
| 0   | 49.57   | 2.47      | 738.32   | Khách phổ thông |
| 1   | 28.50   | 8.07      | 3133.57  | Khách hàng VIP |
| 2   | 251.49  | 1.44      | 410.44   | Khách hàng đã rời bỏ |

> Nhóm VIP (Cluster 1) là khách mua gần đây, thường xuyên và chi tiêu cao — nhóm nên được giữ chân ưu tiên.

---

## 🧾 Công nghệ sử dụng

- Python (Pandas, Scikit-learn, Matplotlib)
- Jupyter Notebook
- Isolation Forest (outlier detection)
- KMeans Clustering (AI Unsupervised)
- Streamlit / Flask (nếu có UI)
