# 📅 Sprint 2 Guide: The Storm Replay (Dòng Chảy Dữ Liệu)
**Mục tiêu:** Tái hiện cơn bão Yagi bằng cách đẩy dữ liệu từ CSV vào Kafka và lưu trữ xuống Data Lake (MinIO) thông qua Spark Streaming.

---

## ⚠️ Lưu Ý Quan Trọng

> **AWS SDK không chấp nhận hostname có dấu gạch dưới (`_`).**
> 
> Tất cả tên container **PHẢI** dùng dấu gạch ngang (`-`) thay vì gạch dưới.
> - ✅ `yagi-kafka`, `yagi-minio`, `yagi-spark-master`
> - ❌ `yagi_kafka`, `yagi_minio`, `yagi_spark_master`

---

## 1. Cấu Hình Docker Compose

### File `docker-compose.yaml` (Phần Kafka)
```yaml
  kafka:
    image: apache/kafka:latest
    container_name: yagi-kafka  # Dùng dấu gạch ngang!
    ports:
      - "9092:9092" # Internal (Spark -> Kafka)
      - "9094:9094" # External (Local Producer -> Kafka)
    environment:
      - KAFKA_NODE_ID=0
      - KAFKA_PROCESS_ROLES=controller,broker
      - KAFKA_CONTROLLER_QUORUM_VOTERS=0@kafka:9093
      - KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093,EXTERNAL://:9094
      - KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://yagi-kafka:9092,EXTERNAL://localhost:9094
      - KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,EXTERNAL:PLAINTEXT
      - KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT
    volumes:
      - kafka_data:/var/lib/kafka/data
    restart: on-failure
```

*Giải thích:*
*   `PLAINTEXT (9092)`: Dành cho các container bên trong (Spark) gọi tới `yagi-kafka:9092`.
*   `EXTERNAL (9094)`: Dành cho máy tính của bạn (Producer) gọi tới `localhost:9094`.

### Apply thay đổi
```bash
docker-compose down
docker-compose up -d
```

---

## 2. Chuẩn Bị Môi Trường Python (Local)
Cài đặt các thư viện cần thiết để chạy Producer trên máy của bạn:

```bash
pip install pandas kafka-python
```

---

## 3. Tạo Bucket MinIO

Trước khi chạy Spark job, phải tạo bucket `yagi-data` trong MinIO:

1. Mở trình duyệt vào `http://localhost:9001`
2. Đăng nhập: `admin` / `password123`
3. Tạo bucket mới có tên `yagi-data`

Hoặc dùng CLI:
```bash
docker exec yagi-minio mc alias set myminio http://localhost:9000 admin password123
docker exec yagi-minio mc mb myminio/yagi-data
```

---

## 4. File Producer: `jobs/yagi_producer.py`

```python
import os
import time
import json
import pandas as pd
from kafka import KafkaProducer

# Cấu hình
KAFKA_TOPIC = "weather-stream"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9094"  # Port External 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "../data/yagi_storm.csv")

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def run_producer():
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        value_serializer=json_serializer
    )
    
    print(f"Reading data from {DATA_PATH}...")
    df = pd.read_csv(DATA_PATH)
    
    print(f"Start sending {len(df)} records to Kafka topic '{KAFKA_TOPIC}'...")
    
    for index, row in df.iterrows():
        record = row.to_dict()
        producer.send(KAFKA_TOPIC, record)
        print(f"Sent: {record['datetime']} - Wind: {record.get('windspeed', 0)} km/h")
        
    producer.flush()
    print("Done!")

if __name__ == "__main__":
    run_producer()
```

---

## 5. File Spark Ingestion: `jobs/spark_ingestion.py`

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType


MINIO_ACCESS_KEY = "admin"
MINIO_SECRET_KEY = "password123"
MINIO_ENDPOINT = "http://yagi-minio:9000"  # Dùng dấu gạch ngang!
KAFKA_BOOTSTRAP_SERVERS = "yagi-kafka:9092"  # Dùng dấu gạch ngang!
TOPIC = "weather-stream"


def main():
    # 1. Khởi tạo Spark Session với cấu hình S3A cho MinIO
    spark = SparkSession.builder \
        .appName("YagiStormIngestion") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.hadoop.fs.s3a.endpoint", MINIO_ENDPOINT) \
        .config("spark.hadoop.fs.s3a.access.key", MINIO_ACCESS_KEY) \
        .config("spark.hadoop.fs.s3a.secret.key", MINIO_SECRET_KEY) \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
        .config("spark.hadoop.fs.s3a.endpoint.region", "us-east-1") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    # 2. Định nghĩa Schema (khớp với cột trong CSV)
    schema = StructType([
        StructField("name", StringType(), True),
        StructField("datetime", StringType(), True),
        StructField("temp", DoubleType(), True),
        StructField("feelslike", DoubleType(), True),
        StructField("dew", DoubleType(), True),
        StructField("humidity", DoubleType(), True),
        StructField("precip", DoubleType(), True),
        StructField("precipprob", DoubleType(), True),
        StructField("preciptype", StringType(), True),
        StructField("snow", DoubleType(), True),
        StructField("snowdepth", DoubleType(), True),
        StructField("windgust", DoubleType(), True),
        StructField("windspeed", DoubleType(), True),
        StructField("winddir", DoubleType(), True),
        StructField("sealevelpressure", DoubleType(), True),
        StructField("cloudcover", DoubleType(), True),
        StructField("visibility", DoubleType(), True),
        StructField("solarradiation", DoubleType(), True),
        StructField("solarenergy", DoubleType(), True),
        StructField("uvindex", DoubleType(), True),
        StructField("severerisk", DoubleType(), True),
        StructField("conditions", StringType(), True),
        StructField("icon", StringType(), True),
        StructField("stations", StringType(), True)
    ])

    # 3. Đọc dữ liệu từ Kafka
    kafka_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
        .option("subscribe", TOPIC) \
        .option("startingOffsets", "earliest") \
        .load()

    # 4. Parse JSON
    parsed_df = kafka_df.select(
        from_json(col("value").cast("string"), schema).alias("data")
    ).select("data.*")

    # 5. Ghi dữ liệu xuống MinIO (Delta Lake)
    query = parsed_df.writeStream \
        .format("delta") \
        .outputMode("append") \
        .option("checkpointLocation", "s3a://yagi-data/checkpoints/weather") \
        .option("path", "s3a://yagi-data/bronze/weather") \
        .start()

    print("Spark Streaming is running... Data is flowing to MinIO.")
    query.awaitTermination()

if __name__ == "__main__":
    main()
```

**Cấu hình quan trọng:**
- `spark.hadoop.fs.s3a.endpoint.region=us-east-1` - **BẮT BUỘC!** AWS SDK cần config này dù MinIO không quan tâm region.

---

## 6. Thực Thi Pipeline

### 🔹 Bước 1: Chạy Producer TRƯỚC (tạo Kafka topic)

```bash
python jobs/yagi_producer.py
```

Đợi cho đến khi thấy `Done!`.

### 🔹 Bước 2: Submit Spark Job

**Cách 1: Chạy từ TRONG container (khuyên dùng)**

```bash
# Vào container
docker exec -it yagi-spark-master bash

# Chạy spark-submit
/opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --conf spark.jars.ivy=/tmp/.ivy \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3,io.delta:delta-spark_2.12:3.1.0,org.apache.hadoop:hadoop-aws:3.3.4 \
  /opt/spark/jobs/spark_ingestion.py
```

**Cách 2: Chạy từ Git Bash (Windows)**

```bash
docker exec -it yagi-spark-master //opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --conf spark.jars.ivy=//tmp/.ivy \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3,io.delta:delta-spark_2.12:3.1.0,org.apache.hadoop:hadoop-aws:3.3.4 \
  //opt/spark/jobs/spark_ingestion.py
```

*(Lưu ý: Dùng `//` ở đầu path để tránh Git Bash tự chuyển đổi đường dẫn)*

### 🔹 Bước 3: Kiểm Tra Kết Quả

1. Xem log Spark - phải thấy: `Spark Streaming is running... Data is flowing to MinIO.`
2. Mở MinIO Console: `http://localhost:9001` (login: `admin` / `password123`)
3. Vào bucket `yagi-data` → thư mục `bronze/weather` → thấy các file `.parquet` là **THÀNH CÔNG!** 🎉

---

## 7. Troubleshooting

| Lỗi | Nguyên nhân | Cách fix |
|-----|-------------|----------|
| `hostname cannot be null` | Hostname có dấu gạch dưới `_` | Đổi tất cả `yagi_*` thành `yagi-*` trong docker-compose.yaml |
| `UnknownTopicOrPartitionException` | Kafka topic chưa tồn tại | Chạy Producer trước để tạo topic |
| `NumberFormatException: "60s"` | Spark version không tương thích | Dùng `apache/spark:3.5.3` |
| `ClassNotFoundException: scala.collection...` | Sai Scala version trong packages | Dùng `_2.12` cho Spark 3.5.x |

---

## 8. Phiên Bản Đã Test Thành Công

| Component | Version |
|-----------|---------|
| Spark | `apache/spark:3.5.3` |
| Kafka | `apache/kafka:latest` |
| MinIO | `minio/minio:latest` |
| Delta Lake | `delta-spark_2.12:3.1.0` |
| Hadoop AWS | `hadoop-aws:3.3.4` |
| Scala | `2.12` |
