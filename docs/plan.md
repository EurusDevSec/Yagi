

---

# 🌪️ PROJECT C.H.A.O.S
**(Climate Hazard Analysis & Operations System)**

### 1. Tên Đề Tài & Định Vị
* **Tên chính thức (Báo cáo):** Xây dựng Hệ thống Data Lakehouse & MLOps End-to-End cho Cảnh báo Biến đổi Khí hậu Thời gian thực.
* **Tên mã (Codename):** Project C.H.A.O.S.
* **Slogan:** *"Biến sự hỗn loạn của dữ liệu thành trật tự của dự báo."*
* **Định vị:** Một hệ thống Big Data hiện đại (SOTA), tích hợp tư duy DevOps/System để giải quyết bài toán khí hậu, vượt xa các đồ án phân tích dữ liệu tĩnh thông thường.

### 2. Mục Tiêu Dự Án (Objectives)
* **Mục tiêu cốt lõi (Core):** Xây dựng thành công Pipeline xử lý dữ liệu lớn từ khâu thu thập (Ingestion) -> lưu trữ (Storage) -> xử lý (Processing) -> dự báo (Prediction) theo thời gian thực (Real-time).
* **Mục tiêu công nghệ (Tech):**
    * [cite_start]Triển khai kiến trúc **Data Lakehouse** (MinIO + Delta Lake)[cite: 7, 13].
    * [cite_start]Ứng dụng **Apache Spark Streaming** cho xử lý luồng[cite: 10, 46].
    * [cite_start]Thiết lập quy trình **MLOps cơ bản** (Train trên Cloud, Deploy dưới Edge)[cite: 79].
    * Chứng minh khả năng chịu lỗi (Resilience) thông qua **Chaos Engineering**.
* **Mục tiêu đầu ra (Deliverable):** Một hệ thống chạy được trên Docker Compose, có Dashboard Real-time hiển thị dữ liệu khí hậu và cảnh báo thiên tai.

### 3. Kiến Trúc Kỹ Thuật (Hybrid Architecture - 16GB RAM Optimized)

* **Ingestion Layer:**
    * *Source:* Dữ liệu lịch sử Kaggle (Hourly Weather Data) giả lập luồng Real-time (Data Replay).
    * *Message Queue:* **Apache Kafka** (Image: `bitnami/kafka`, KRaft Mode - No Zookeeper).
* **Storage Layer (Data Lakehouse):**
    * [cite_start]*Object Storage:* **MinIO** (Giả lập S3)[cite: 15].
    * [cite_start]*Table Format:* **Delta Lake** (Hỗ trợ ACID & Time-travel)[cite: 7, 15].
* **Processing Layer:**
    * [cite_start]*Engine:* **Apache Spark (PySpark)** chạy chế độ Streaming[cite: 5].
* **Intelligence Layer (MLOps):**
    * [cite_start]*Training:* **Google Colab** (Sử dụng Spark MLlib để train model dự báo)[cite: 5].
    * *Serving:* Python Script load model đã train để dự báo realtime.
* **Presentation Layer:**
    * *Dashboard:* **Streamlit** (Python).
    * *Alerting:* Telegram Bot (Optional).
* **Infrastructure:**
    * **Docker Compose** để quản lý toàn bộ service.
    * **Monitoring:** **Portainer** (Container Management UI).

---

### 4. Kế Hoạch Thực Hiện Chi Tiết (4-Week Agile Sprint)

#### 📅 Sprint 1: The Foundation - Xây Dựng Hạ Tầng Container
* **Mục tiêu:** Dựng xong cụm Cluster ảo trên máy local. Lệnh `docker-compose up` phải chạy mượt mà, không sập nguồn vì thiếu RAM.
* **Công việc cụ thể:**
    1.  Cài đặt môi trường: Docker Desktop, Python 3.9+, Java (nếu cần debug).
    2.  Thiết kế file `docker-compose.yaml`:
        * Cấu hình **Kafka (KRaft Mode)**: Loại bỏ Zookeeper giúp tiết kiệm ~500MB-1GB RAM.
        * Cấu hình **Portainer**: Thêm container Portainer để monitoring trực quan.
        * Cấu hình **MinIO**: Thiết lập Access Key/Secret Key, tạo sẵn Bucket `climate-data`.
        * Cấu hình **Spark Master & Worker**: Giới hạn Worker RAM tối đa 4GB.
    3.  Kiểm thử (Smoke Test):
        * Dùng Kafka Tool kết nối port 9092.
        * Truy cập MinIO Console (localhost:9001).
        * Truy cập Spark UI (localhost:8080).

#### 📅 Sprint 2: The Flow - Dòng Chảy Dữ Liệu "Data Replay"
* **Mục tiêu:** Dữ liệu từ file Kaggle phải "chảy" vào MinIO dưới dạng Delta Lake theo thời gian thực.
* **Công việc cụ thể:**
    1.  Chuẩn bị dữ liệu: Tải dataset **"Hourly Weather Data"** từ Kaggle.
    2.  Viết `replay_producer.py`:
        * Đọc tuần tự từng dòng CSV.
        * Thay thế timestamp cũ bằng `datetime.now()`.
        * Đẩy vào Kafka Topic `weather-realtime`.
    3.  Viết `ingestion_job.py` (Spark Streaming):
        * Đọc từ Kafka `weather-realtime`.
        * Parse JSON/CSV.
        * Ghi xuống MinIO bucket `climate-data` định dạng **Delta Lake**.
    4.  Kiểm chứng: Thấy file `.parquet` sinh ra liên tục trong MinIO.

#### 📅 Sprint 3: The Brain - Trí Tuệ Lai (Hybrid MLOps)
* **Mục tiêu:** Train model trên Cloud (Colab) và mang về Local deploy.
* **Công việc cụ thể:**
    1.  Xuất dữ liệu: Copy một lượng dữ liệu lịch sử từ MinIO (hoặc dùng chính file Kaggle gốc) upload lên Google Drive.
    2.  Training trên Colab:
        * Dùng **PySpark MLlib**.
        * Bài toán: Dự báo nhiệt độ giờ tiếp theo (Regression) hoặc Phân loại rủi ro bão (Classification).
        * Export model đã train (`.zip` hoặc folder).
    3.  Deploy tại Local (Inference Service):
        * Viết `prediction_service.py`.
        * Load model từ file đã tải về.
        * Subscribe Kafka `weather-realtime` -> Predict -> Publish kết quả vào Kafka `alert-data`.

#### 📅 Sprint 4: The Face & The Chaos - Hiển Thị & Khả Năng Chịu Lỗi
* **Mục tiêu:** Dashboard đẹp, demo hệ thống tự phục hồi (Self-healing).
* **Công việc cụ thể:**
    1.  Xây dựng Dashboard (**Streamlit**):
        * Biểu đồ line chart: Nhiệt độ thực tế vs. Dự báo.
        * Chỉ số cảnh báo: Màu đỏ khi nhiệt độ/độ ẩm vượt ngưỡng.
    2.  Thực hiện **Chaos Engineering**:
        * Cấu hình Docker `restart: always`.
        * Viết script `chaos_monkey.py`: Random kill container `prediction_service`.
    3.  Tổng diễn tập Demo:
        * Bật hệ thống -> Chạy Data Replay -> Show Dashboard.
        * Mở **Portainer**: Quan sát trạng thái container.
        * Kill service (Chaos Monkey) -> Xem trên Portainer thấy container tự restart (Self-healing).

---

### 5. Tech Stack Chốt Hạ (Tối ưu 16GB RAM)
* **Language:** Python (PySpark, Streamlit).
* **Big Data:** Apache Spark 3.x, Apache Kafka 3.x (KRaft Mode).
* **Storage:** MinIO, Delta Lake 2.x.
* **DevOps:** Docker, Docker Compose, Portainer.
* **Cloud:** Google Colab (cho Training).

