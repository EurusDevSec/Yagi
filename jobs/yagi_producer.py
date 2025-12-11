import time 
import json
import pandas as pd
from kafka import KafkaProducer


KAFKA_TOPIC = "weather-stream"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9094" # Port External
DATA_PATH = "../data/yagi_storm.csv" # Đường dẫn tới file CSV
SPEED_FACTOR = 1 # 1 = Real-time, 10 = Nhanh gấp 10 lần


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def run_producer():
    # 1. Khởi tạo Producer
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        value_serializer=json_serializer
    )
    
    # 2. Đọc dữ liệu
    print(f"Reading data from {DATA_PATH}...")
    df = pd.read_csv(DATA_PATH)
    # Lọc các cột cần thiết nếu cần (datetime, wind_kph, pressure_mb, ...)
    # df = df[['datetime', 'wind_kph', 'pressure_mb', 'precip_mm', 'humidity']]
    
    print(f"Start sending {len(df)} records to Kafka topic '{KAFKA_TOPIC}'...")
    
    for index, row in df.iterrows():
        record = row.to_dict()
        
        # Gửi tin nhắn
        producer.send(KAFKA_TOPIC, record)
        print(f"Sent: {record['datetime']} - Wind: {record.get('wind_kph', 0)} km/h")
        
        # Giả lập delay (nếu cần chính xác theo timestamp thì code phức tạp hơn, ở đây ta sleep tượng trưng)
        time.sleep(1 / SPEED_FACTOR)
        
    producer.flush()
    print("Done!")

if __name__ == "__main__":
    run_producer()
