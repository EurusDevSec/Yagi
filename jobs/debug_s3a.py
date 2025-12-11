from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DebugS3A") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://yagi_minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "password123") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .getOrCreate()

# Debug - in ra cấu hình Hadoop
hadoop_conf = spark.sparkContext._jsc.hadoopConfiguration()
print("=== S3A Configuration ===")
print(f"fs.s3a.endpoint = {hadoop_conf.get('fs.s3a.endpoint')}")
print(f"fs.s3a.access.key = {hadoop_conf.get('fs.s3a.access.key')}")
print(f"fs.s3a.path.style.access = {hadoop_conf.get('fs.s3a.path.style.access')}")
print(f"fs.s3a.impl = {hadoop_conf.get('fs.s3a.impl')}")

spark.stop()
