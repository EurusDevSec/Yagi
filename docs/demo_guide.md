# 🚀 Kịch Bản Demo Dự Án Y.A.G.I (Quick Start)

Tài liệu này hướng dẫn các bước ngắn gọn để trình bày demo mượt mà, giả định bạn đã cài đặt và build xong mọi thứ.

---

## 1. Chuẩn bị (Trước giờ G)

1.  Mở **Docker Desktop**.
2.  Mở **VS Code** tại thư mục dự án `Yagi`.
3.  Mở sẵn **2 tab Terminal** (Terminal 1 để quản lý Docker, Terminal 2 để chạy Producer).

---

## 2. Bắt đầu Demo (Showtime)

### Bước 1: Khởi động hệ thống (Terminal 1)

Chạy lệnh sau để bật toàn bộ các dịch vụ (Kafka, Predictor, Dashboard...):

```bash
docker-compose up -d
```

_Chờ khoảng 30s để các service khởi động hoàn toàn._

### Bước 2: Kiểm tra trạng thái (Terminal 1)

Kiểm tra xem `predictor` đã kết nối Kafka thành công chưa:

```bash
docker logs -f yagi-predictor
```

- _Dấu hiệu thành công:_ Thấy dòng `✅ Manually assigned to partitions...`.
- _Thoát xem log:_ Nhấn `Ctrl + C`.

### Bước 3: Mở Dashboard

1.  Mở trình duyệt truy cập: [http://localhost:8501](http://localhost:8501)
2.  Nhấn nút **"Bắt đầu giám sát"**.
3.  Lúc này Dashboard sẽ hiện trạng thái "Đã kết nối Kafka" và chờ dữ liệu.

### Bước 4: Bơm dữ liệu bão (Terminal 2)

Chạy script giả lập dữ liệu từ cảm biến gửi về:

```bash
python jobs/yagi_producer.py
```

👉 **Lúc này hãy chuyển sang màn hình Dashboard để cho giảng viên thấy biểu đồ và các chỉ số nhảy múa theo thời gian thực.**

---

## 3. Reset (Nếu muốn chạy lại demo lần 2)

Nếu bạn muốn làm mới lại phiên trình bày (xóa biểu đồ cũ trên màn hình):

1.  Dừng Producer ở Terminal 2 (`Ctrl + C`).
2.  Khởi động lại container Dashboard để xóa bộ nhớ tạm:
    ```bash
    docker-compose restart dashboard
    ```
3.  Reload lại trang web và làm lại từ **Bước 3**.
