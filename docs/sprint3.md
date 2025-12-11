# 📅 Sprint 3 Guide: The Intelligence (MLOps Logic)
**Mục tiêu:** Hệ thống có "não" - Train model dự báo bão và deploy prediction service để cảnh báo thời gian thực.

---

## 📋 Yêu Cầu Trước Khi Bắt Đầu

- ✅ Hoàn thành Sprint 2 (dữ liệu đã chảy vào MinIO Delta Lake)
- ✅ Docker containers đang chạy (`docker-compose up -d`)
- ✅ Có Google account để dùng Colab

---

## 1. Train Model trên Google Colab

### Bước 1.1: Tạo Notebook mới

Truy cập [Google Colab](https://colab.research.google.com/) và tạo notebook mới.

### Bước 1.2: Upload dữ liệu training

```python
from google.colab import files
uploaded = files.upload()  # Upload file yagi_storm.csv
```

### Bước 1.3: Code Training Model

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
import joblib

# 1. Load dữ liệu
df = pd.read_csv('yagi_storm.csv')
print(f"Dataset shape: {df.shape}")
print(df.columns.tolist())  # Xem tất cả tên cột
print(df.head())

# 2. Feature Engineering
# Tạo label: 1 = Nguy hiểm (gió > 60km/h), 0 = An toàn
# Lưu ý: Cột gió là 'windspeed' không phải 'wind_kph'
df['is_dangerous'] = (df['windspeed'] > 60).astype(int)

# Features để predict (dùng đúng tên cột từ CSV)
features = ['temp', 'sealevelpressure', 'humidity', 'cloudcover', 'precip', 'windgust']
X = df[features].fillna(0)
y = df['is_dangerous']

print(f"\nDangerous records: {y.sum()} / {len(y)}")

# 3. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train Classification Model (Nguy hiểm hay không?)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 5. Evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2%}")

# 6. Feature Importance
importance = pd.DataFrame({
    'feature': features,
    'importance': clf.feature_importances_
}).sort_values('importance', ascending=False)
print("\nFeature Importance:")
print(importance)

# 7. Save Model
joblib.dump(clf, 'storm_classifier.pkl')
print("\n✅ Model saved to storm_classifier.pkl")

# 8. Download model
files.download('storm_classifier.pkl')
```

### Bước 1.4: (Optional) Train Regression Model

Nếu muốn dự báo sức gió thay vì phân loại:

```python
# Regression: Predict wind speed
# Dùng đúng tên cột từ CSV
X_reg = df[['temp', 'sealevelpressure', 'humidity', 'cloudcover', 'precip', 'windgust']].fillna(0)
y_reg = df['windspeed'].fillna(0)

X_train, X_test, y_train, y_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

reg = GradientBoostingRegressor(n_estimators=100, random_state=42)
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.2f} km/h")

joblib.dump(reg, 'storm_regressor.pkl')
files.download('storm_regressor.pkl')
```

---

## 2. Deploy Prediction Service

### Bước 2.1: Tạo thư mục cho Predictor

```bash
mkdir -p predictor
```

### Bước 2.2: Copy model vào thư mục

Đặt file `storm_classifier.pkl` (đã download từ Colab) vào thư mục `predictor/`.

### Bước 2.3: Tạo file `predictor/predictor.py`

```python
import json
import time
import joblib
import numpy as np
from kafka import KafkaConsumer, KafkaProducer

# Cấu hình
KAFKA_BOOTSTRAP_SERVERS = "yagi-kafka:9092"
INPUT_TOPIC = "weather-stream"
ALERT_TOPIC = "storm-alerts"
MODEL_PATH = "/app/storm_classifier.pkl"

# Ngưỡng cảnh báo
WIND_THRESHOLD = 60  # km/h

def load_model():
    """Load trained model"""
    try:
        model = joblib.load(MODEL_PATH)
        print(f"✅ Model loaded from {MODEL_PATH}")
        return model
    except FileNotFoundError:
        print(f"⚠️ Model not found at {MODEL_PATH}, using rule-based prediction")
        return None

def create_alert(record, prediction, confidence=None):
    """Tạo message cảnh báo"""
    alert_level = "🔴 CRITICAL" if prediction == 1 else "🟢 SAFE"
    
    alert = {
        "timestamp": record.get("datetime", time.strftime("%Y-%m-%d %H:%M:%S")),
        "alert_level": alert_level,
        "is_dangerous": bool(prediction),
        "windspeed": record.get("windspeed", 0),
        "sealevelpressure": record.get("sealevelpressure", 0),
        "humidity": record.get("humidity", 0),
        "message": f"Wind speed: {record.get('windspeed', 0)} km/h"
    }
    
    if confidence is not None:
        alert["confidence"] = f"{confidence:.2%}"
    
    return alert

def rule_based_predict(record):
    """Fallback: Rule-based prediction nếu không có model"""
    wind = record.get("windspeed", 0) or 0
    pressure = record.get("sealevelpressure", 1013) or 1013
    
    # Gió > 60km/h HOẶC áp suất < 990mb = Nguy hiểm
    if wind > WIND_THRESHOLD or pressure < 990:
        return 1
    return 0

def main():
    print("🚀 Storm Predictor Service Starting...")
    
    # Load model
    model = load_model()
    
    # Kafka Consumer
    consumer = KafkaConsumer(
        INPUT_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='latest',
        group_id='predictor-group'
    )
    
    # Kafka Producer (for alerts)
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    print(f"📡 Listening to topic: {INPUT_TOPIC}")
    print(f"📢 Alerts will be sent to: {ALERT_TOPIC}")
    
    for message in consumer:
        record = message.value
        
        try:
            if model is not None:
                # ML-based prediction (dùng đúng tên cột từ CSV)
                features = np.array([[
                    record.get('temp', 0) or 0,
                    record.get('sealevelpressure', 1013) or 1013,
                    record.get('humidity', 50) or 50,
                    record.get('cloudcover', 0) or 0,
                    record.get('precip', 0) or 0,
                    record.get('windgust', 0) or 0
                ]])
                prediction = model.predict(features)[0]
                proba = model.predict_proba(features)[0]
                confidence = max(proba)
            else:
                # Rule-based fallback
                prediction = rule_based_predict(record)
                confidence = None
            
            # Tạo và gửi alert
            alert = create_alert(record, prediction, confidence)
            producer.send(ALERT_TOPIC, alert)
            
            # Log
            status = "⚠️ DANGEROUS" if prediction == 1 else "✅ Safe"
            print(f"{record.get('datetime')} | Wind: {record.get('windspeed', 0):>6} km/h | {status}")
            
        except Exception as e:
            print(f"❌ Error processing: {e}")
            continue
    
    consumer.close()
    producer.close()

if __name__ == "__main__":
    main()
```

### Bước 2.4: Tạo file `predictor/requirements.txt`

```
kafka-python
scikit-learn
joblib
numpy
pandas
```

### Bước 2.5: Tạo file `predictor/Dockerfile`

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements và install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model và code
COPY storm_classifier.pkl .
COPY predictor.py .

# Run
CMD ["python", "predictor.py"]
```

### Bước 2.6: Cập nhật `docker-compose.yaml`

Thêm service `predictor` vào cuối file (trước `volumes:`):

```yaml
  # --- Prediction Service ---
  predictor:
    build: ./predictor
    container_name: yagi-predictor
    depends_on:
      - kafka
    restart: on-failure
    environment:
      - PYTHONUNBUFFERED=1
```

---

## 3. Thực Thi

### Bước 3.1: Build và start Predictor

```bash
# Build image
docker-compose build predictor

# Start all services
docker-compose up -d
```

### Bước 3.2: Kiểm tra Predictor đang chạy

```bash
docker logs -f yagi-predictor
```

Bạn sẽ thấy:
```
🚀 Storm Predictor Service Starting...
✅ Model loaded from /app/storm_classifier.pkl
📡 Listening to topic: weather-stream
📢 Alerts will be sent to: storm-alerts
```

### Bước 3.3: Chạy Producer để test

```bash
python jobs/yagi_producer.py
```

### Bước 3.4: Xem kết quả prediction

```bash
docker logs -f yagi-predictor
```

Output sẽ như:
```
2024-09-05T00:00:00 | Wind:      0 km/h | ✅ Safe
2024-09-05T01:00:00 | Wind:      0 km/h | ✅ Safe
...
2024-09-07T15:00:00 | Wind:     85 km/h | ⚠️ DANGEROUS
2024-09-07T16:00:00 | Wind:    102 km/h | ⚠️ DANGEROUS
```

---

## 4. Đọc Alert Topic (Optional)

Tạo file `jobs/alert_consumer.py` để xem các cảnh báo:

```python
import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'storm-alerts',
    bootstrap_servers='localhost:9094',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest'
)

print("🔔 Listening for alerts...")
for msg in consumer:
    alert = msg.value
    if alert['is_dangerous']:
        print(f"🔴 {alert['timestamp']} | {alert['message']} | {alert.get('confidence', 'N/A')}")
    else:
        print(f"🟢 {alert['timestamp']} | {alert['message']}")
```

Chạy:
```bash
python jobs/alert_consumer.py
```

---

## 5. Cấu Trúc Thư Mục Sau Sprint 3

```
Yagi/
├── docker-compose.yaml
├── data/
│   └── yagi_storm.csv
├── jobs/
│   ├── yagi_producer.py
│   ├── spark_ingestion.py
│   └── alert_consumer.py      # Mới
├── predictor/                  # Mới
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── predictor.py
│   └── storm_classifier.pkl   # Model từ Colab
└── docs/
    ├── plan.md
    ├── sprint1.md
    ├── sprint2.md
    └── sprint3.md
```

---

## 6. Troubleshooting

| Lỗi | Nguyên nhân | Cách fix |
|-----|-------------|----------|
| `Model not found` | Chưa copy file `.pkl` vào predictor/ | Copy model từ Colab vào thư mục predictor/ |
| `NoBrokersAvailable` | Kafka chưa sẵn sàng | Đợi Kafka khởi động xong hoặc thêm retry logic |
| `docker-compose build` lỗi | Thiếu Dockerfile hoặc requirements.txt | Kiểm tra lại cấu trúc thư mục predictor/ |

---

## 7. Kết Quả Mong Đợi

- [x] Model được train trên Colab với accuracy > 80%
- [x] Predictor service chạy trong Docker
- [x] Predictor consume từ `weather-stream`, predict, và publish lên `storm-alerts`
- [x] Console hiển thị trạng thái Safe/Dangerous cho mỗi bản ghi

---

## ➡️ Tiếp theo: Sprint 4

Sprint 4 sẽ tập trung vào:
- Dashboard Streamlit hiển thị real-time
- Tích hợp Telegram Bot gửi cảnh báo
- Chaos Engineering Test (tắt container, kiểm tra tự phục hồi)
