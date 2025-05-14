import os
from pyspark.sql import SparkSession

print("JAVA_HOME:", os.environ.get("JAVA_HOME"))
print("HADOOP_HOME:", os.environ.get("HADOOP_HOME"))
print("PATH:", os.environ.get("PATH"))

try:
    print("Testing java version...")
    os.system("java -version")
except Exception as e:
    print("Java error:", str(e))

try:
    print("Testing winutils...")
    os.system('"C:\\hadoop\\bin\\winutils.exe" dir')
except Exception as e:
    print("Winutils error:", str(e))

spark = SparkSession.builder \
    .appName("MinimalTest") \
    .master("local[*]") \
    .config("spark.hadoop.home", "C:\hadoop") \
    .getOrCreate()

df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])
df.show()
spark.stop()