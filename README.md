# 🧠 ỨNG DỤNG AI PHÂN LOẠI PHÂN KHÚC KHÁCH HÀNG TRONG LĨNH VỰC BÁN LẺ TRỰC TUYẾN DỰA TRÊN DỮ LIỆU UCI

> **Sinh viên thực hiện:** Nguyễn Sơn Tùng – NEU  
> **Môn học:** Phát triển các hệ thống thông tin quản lý  
> **Trường:** Đại học Kinh tế Quốc Dân  
> **Thời gian:** 1/2025 – 05/2025
> ---

## 📌 Giới thiệu
Dự án này sử dụng **trí tuệ nhân tạo (AI)**, cụ thể là **thuật toán phân cụm K-Means** kết hợp với mô hình **RFM (Recency - Frequency - Monetary)** để phân loại khách hàng trong lĩnh vực bán lẻ trực tuyến. Dữ liệu được lấy từ **UCI Machine Learning Repository**.

---

## 🎯 Mục tiêu
- Xây dựng mô hình phân cụm khách hàng dựa trên hành vi tiêu dùng.
- Tối ưu hóa chiến lược marketing theo từng nhóm khách hàng cụ thể.
- Tích hợp hệ thống đầu vào thủ công và qua file CSV giúp dễ sử dụng.

---

## 🛠️ Công nghệ sử dụng
- Python: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
- Streamlit (giao diện người dùng)
- Jupyter Notebook (phân tích và thử nghiệm)
- Google Colab hoặc VS Code

---

## 📊 Mô tả dữ liệu
**Dataset**: Online Retail (UCI)  
**Thời gian**: 01/12/2010 - 09/12/2011  
**Các cột chính**:
- InvoiceNo, StockCode, Description
- Quantity, InvoiceDate, UnitPrice
- CustomerID, Country

---

## ⚙️ Quy trình thực hiện
1. **Tiền xử lý dữ liệu**
   - Xoá bản ghi không hợp lệ (hủy đơn, thiếu CustomerID,...)
   - Phát hiện và loại bỏ ngoại lệ bằng Isolation Forest

2. **Tạo đặc trưng RFM**
   - Recency: Số ngày từ lần mua gần nhất
   - Frequency: Số lần mua hàng
   - Monetary: Tổng chi tiêu

3. **Chuẩn hóa dữ liệu**
   - Sử dụng `StandardScaler` để scale RFM

4. **Phân cụm bằng KMeans**
   - Dùng Elbow Method để chọn K = 3
   - Phân thành 3 nhóm khách hàng:
     - Khách phổ thông
     - Khách VIP
     - Khách rời bỏ

5. **Đánh giá mô hình**
   - Silhouette Score: `0.484`
   - Calinski-Harabasz: `4576.92`
   - Davies-Bouldin: `0.728`

6. **Xây dựng giao diện**
   - Nhập tay từng khách (Recency, Frequency, Monetary)
   - Tải file CSV để phân tích hàng loạt

---

## 🖥️ Giao diện người dùng (Streamlit)
- **Thủ công**: nhập RFM để kiểm tra 1 khách hàng
- **CSV**: xuất bảng gồm CustomerID, R, F, M và Cụm (Cluster)

---

## 📁 Cấu trúc thư mục
