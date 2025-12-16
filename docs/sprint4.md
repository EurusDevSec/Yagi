# 📅 Sprint 4 Guide: The Interface & Resilience (Giao Diện & Chịu Lỗi)

**Mục tiêu:** Xây dựng Dashboard theo dõi bão thời gian thực và kiểm thử khả năng tự phục hồi của hệ thống.

---

## 📋 Yêu Cầu Trước Khi Bắt Đầu

- ✅ Hoàn thành Sprint 3 (Predictor Service đã chạy ổn định).
- ✅ Docker containers đang chạy (`kafka`, `predictor`, v.v.).

---

## 1. Xây Dựng Dashboard (Streamlit)

Chúng ta sẽ tạo một service mới tên là `dashboard` để hiển thị dữ liệu từ Kafka lên biểu đồ.

### Bước 1.1: Tạo cấu trúc thư mục

Tại thư mục gốc dự án, tạo thư mục `dashboard`:

```bash
mkdir dashboard
```

### Bước 1.2: Tạo file `dashboard/requirements.txt`

```text
streamlit
kafka-python
pandas
altair
watchdog
```

### Bước 1.3: Tạo file `dashboard/Dockerfile`

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
```

### Bước 1.4: Tạo file `dashboard/app.py`

Đây là trái tim của giao diện. Nó sẽ đọc dữ liệu từ Kafka topic `weather-stream` và `storm-alerts` để vẽ biểu đồ.

```python
import streamlit as st
import pandas as pd
import json
from kafka import KafkaConsumer
import time
from datetime import datetime

# Cấu hình trang
st.set_page_config(
    page_title="YAGI Storm Monitor",
    page_icon="🌪️",
    layout="wide"
)

# Tiêu đề
st.title("🌪️ YAGI Storm Real-time Monitor")
st.markdown("Hệ thống giám sát và cảnh báo bão thời gian thực")

# Cấu hình Kafka
KAFKA_BOOTSTRAP_SERVERS = 'yagi-kafka:9092'
TOPIC_WEATHER = 'weather-stream'
TOPIC_ALERTS = 'storm-alerts'

# Hàm nhận dữ liệu từ Kafka (giả lập polling để không block UI)
# Lưu ý: Streamlit hoạt động theo cơ chế rerun, nên việc tích hợp Kafka consumer trực tiếp
# cần khéo léo. Ở đây ta dùng placeholder để update.

# Tạo các placeholder cho UI
col1, col2, col3 = st.columns(3)
with col1:
    metric_wind = st.empty()
with col2:
    metric_pressure = st.empty()
with col3:
    metric_status = st.empty()

st.divider()

col_chart_1, col_chart_2 = st.columns(2)
with col_chart_1:
    st.subheader("Tốc độ gió (km/h)")
    chart_wind = st.line_chart(x=None, y=None, height=300)

with col_chart_2:
    st.subheader("Áp suất khí quyển (mb)")
    chart_pressure = st.line_chart(x=None, y=None, height=300)

st.subheader("🚨 Nhật ký Cảnh báo")
alert_log = st.empty()

# Khởi tạo session state để lưu dữ liệu
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['timestamp', 'windspeed', 'pressure'])
if 'alerts' not in st.session_state:
    st.session_state.alerts = []

def consume_data():
    consumer = KafkaConsumer(
        TOPIC_WEATHER,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='latest', # Chỉ đọc dữ liệu mới nhất
        group_id='dashboard-group-v1',
        consumer_timeout_ms=100 # Không chờ quá lâu
    )

    # Lấy dữ liệu mới
    new_rows = []
    for message in consumer:
        record = message.value
        timestamp = record.get('datetime')
        wind = record.get('windspeed', 0)
        pressure = record.get('sealevelpressure', 0)

        new_rows.append({
            'timestamp': timestamp,
            'windspeed': wind,
            'pressure': pressure
        })

        # Update Metrics ngay lập tức
        metric_wind.metric("Gió", f"{wind} km/h", delta_color="inverse")
        metric_pressure.metric("Áp suất", f"{pressure} mb")

        if wind > 60:
            metric_status.error("⚠️ NGUY HIỂM")
        else:
            metric_status.success("✅ AN TOÀN")

    # Cập nhật DataFrame
    if new_rows:
        new_df = pd.DataFrame(new_rows)
        st.session_state.data = pd.concat([st.session_state.data, new_df], ignore_index=True).tail(100) # Giữ 100 điểm dữ liệu cuối

        # Vẽ lại biểu đồ
        chart_wind.line_chart(st.session_state.data.set_index('timestamp')['windspeed'])
        chart_pressure.line_chart(st.session_state.data.set_index('timestamp')['pressure'])

# Nút để chạy (Streamlit tự động rerun nhưng ta cần vòng lặp cho Kafka)
if st.button('Bắt đầu giám sát'):
    st.success("Đang kết nối Kafka...")
    while True:
        consume_data()
        time.sleep(1)
```

### Bước 1.5: Cập nhật `docker-compose.yaml`

Thêm service `dashboard` vào file `docker-compose.yaml`:

```yaml
# ... (các service cũ)

# --- Visualization ---
dashboard:
  build: ./dashboard
  container_name: yagi-dashboard
  ports:
    - "8501:8501"
  depends_on:
    - kafka
  restart: always
```

### Bước 1.6: Chạy Dashboard

1.  Build và chạy container:
    ```bash
    docker-compose up -d --build dashboard
    ```
2.  Truy cập trình duyệt: `http://localhost:8501`
3.  Nhấn nút **"Bắt đầu giám sát"**.
4.  Chạy `python jobs/yagi_producer.py` ở terminal khác để bơm dữ liệu và xem biểu đồ nhảy múa!

---

## 2. Tích hợp Telegram Alert (Nâng cao)

Để nhận tin nhắn cảnh báo về điện thoại.

### Bước 2.1: Tạo Bot Telegram

1.  Chat với **@BotFather** trên Telegram.
2.  Gõ `/newbot` -> Đặt tên -> Nhận **TOKEN**.
3.  Tạo một group chat, add con bot vào.
4.  Lấy **Chat ID** của group (có thể dùng @userinfobot hoặc xem API).

### Bước 2.2: Cập nhật `predictor/predictor.py`

Thêm hàm gửi Telegram:

```python
import requests

TELEGRAM_TOKEN = "YOUR_TOKEN_HERE"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Failed to send Telegram: {e}")

# ... Trong vòng lặp xử lý, chỗ tạo alert:
if prediction == 1:
    msg = f"🚨 **CẢNH BÁO BÃO YAGI**\n\nThời gian: {record['datetime']}\nGió: {record['windspeed']} km/h\nCấp độ: NGUY HIỂM"
    send_telegram_alert(msg)
```

---

## 3. Chaos Engineering (Kiểm thử chịu lỗi)

Mục tiêu: Chứng minh hệ thống không chết khi một thành phần bị lỗi.

### Kịch bản: "Sát thủ" Predictor

1.  Đảm bảo hệ thống đang chạy, Dashboard đang hiển thị, Producer đang bắn tin.
2.  Mở terminal, giết chết container `predictor`:
    ```bash
    docker kill yagi-predictor
    ```
3.  Quan sát:
    - Dashboard: Vẫn hiển thị dữ liệu cũ, không bị crash.
    - Docker: Vì ta để `restart: on-failure` (hoặc `always`), Docker sẽ tự động khởi động lại `predictor`.
4.  Kiểm tra log:
    ```bash
    docker logs -f yagi-predictor
    ```
    - Thấy service khởi động lại, kết nối lại Kafka và tiếp tục xử lý.

---

## 🎉 Tổng Kết Dự Án

Bạn đã hoàn thành xây dựng hệ thống **Y.A.G.I** End-to-End:

1.  **Ingestion:** Kafka KRaft nhận dữ liệu tốc độ cao.
2.  **Storage:** MinIO lưu trữ Data Lake.
3.  **Processing:** Spark xử lý dữ liệu.
4.  **Intelligence:** Predictor Service dự báo bão bằng AI.
5.  **Visualization:** Dashboard theo dõi thời gian thực.
6.  **Resilience:** Hệ thống tự phục hồi sau sự cố.
