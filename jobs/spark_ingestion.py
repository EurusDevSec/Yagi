from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType


MINIO_ACCESS_KEY = "admin"
MINIO_SECRET_KEY = "password123"
MINIO_ENDPOINT = "http://yagi-minio:9000"
KAFKA_BOOTSTRAP_SERVERS = "yagi-kafka:9092" # Port Internal
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

    # 2. Định nghĩa Schema (Khớp với cột trong CSV)
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