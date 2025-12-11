from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TestS3A") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://yagi_minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "password123") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .getOrCreate()

# Test đơn giản - tạo DataFrame và ghi ra Parquet
df = spark.createDataFrame([("test", 1), ("hello", 2)], ["name", "value"])
print("DataFrame created successfully")

# Thử ghi ra S3A
df.write.mode("overwrite").parquet("s3a://yagi-data/test-output")
print("Write to S3A successful!")

spark.stop()
