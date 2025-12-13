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