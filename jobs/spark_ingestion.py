from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType


MINIO_ACCESS_KEY = "admin"
MINIO_SECRET_KEY = "password123"
MINIO_ENDPOINT = "http://yagi_minio:9000"
KAFKA_BOOTSTRAP_SERVERS = "yagi_kafka:9092" # Port Internal
TOPIC = "weather-stream"


def 