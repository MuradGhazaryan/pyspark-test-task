# test_spark.py
# This script demonstrates basic PySpark functionality: creating a DataFrame, displaying it, and performing a simple filter operation.

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("TestApp").master("local[1]").getOrCreate()

# Create a sample dataset
data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Cathy", 28),
    ("David", 22)
]
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Display the original DataFrame
print("Original DataFrame:")
df.show()

# Filter the DataFrame to show only people older than 25
df_filtered = df.filter(df["Age"] > 25)
print("Filtered DataFrame (Age > 25):")
df_filtered.show()

# Stop the Spark session
spark.stop()