from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Read SQLite with PySpark") \
    .config("spark.driver.extraClassPath", "/path/to/sqlite-jdbc-3.34.0.jar") \
    .getOrCreate()

db_path = "jdbc:sqlite:data_cua_thang.db"

df = spark.read.format("jdbc") \
    .option("url", db_path) \
    .option("dbtable", "mydata") \
    .option("driver", "org.sqlite.JDBC") \
    .load()

df.show(10)

spark.stop()