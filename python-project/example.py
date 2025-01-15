from pyspark.sql import SparkSession

# Initialize the Spark session
spark = SparkSession.builder \
    .appName("Docker-Spark-Example") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Reading a CSV file from the mounted directory
data_path = "/tmp/data/example.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Show the data
df.show()

# Perform a transformation
df_filtered = df.filter(df["Age"] > 30)

# Write the results back to the mounted directory
output_path = "/tmp/data/output"
df_filtered.write.csv(output_path, mode="overwrite", header=True)

# Stop the Spark session
spark.stop()
