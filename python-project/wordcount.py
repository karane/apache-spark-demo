from pyspark.sql import SparkSession

# SPARK_URL = "spark://spark-master:7077"
SPARK_URL = "spark://localhost:7077"

# Initialize the Spark session
spark = SparkSession.builder \
    .appName("Docker-Spark-Example") \
    .master(SPARK_URL) \
    .getOrCreate()

# Example data
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]

# Create a DataFrame
df = spark.createDataFrame(data, columns)

# Perform operations
df.show()
df.filter(df.Age > 30).show()

# Stop the Spark session
spark.stop()
