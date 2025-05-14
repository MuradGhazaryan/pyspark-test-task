# PySpark Test Task

## Overview
This repository contains a solution for a PySpark test task.  
The script `test_spark.py` demonstrates basic PySpark functionality: creating a DataFrame, displaying it, and performing a simple filter operation.

## Requirements
- Python 3.10.11
- PySpark 3.4.0
- Spark 3.4.4 (pre-built for Hadoop 3)
- Virtual environment (recommended)
- Windows OS (instructions below are Windows-specific)

## Project Structure
```
product_categories/
├── .gitignore # Git ignore rules
├── README.md # Project documentation
├── requirements.txt # Python dependencies
├── solution.py # Main solution logic
├── test_solution.py # Test for solution.py
├── test_spark.py # PySpark example script
├── __pycache__/ # Python cache (ignored)
├── .venv*/ # Virtual environments (ignored)
```

## Setup Instructions

1. **Install Python 3.10.11**  
   Ensure Python 3.10.11 is installed on your system and available in your system PATH.

2. **Create and activate a virtual environment**  
   Run the following commands in PowerShell:
   ```powershell
   python -m venv .venv_py310
   .\.venv_py310\Scripts\activate
   ```

3. **Install PySpark**  
   Inside the activated virtual environment, install PySpark:
   ```powershell
   pip install pyspark==3.4.0
   ```

4. **Download and configure Apache Spark**  
   - Download [Spark 3.4.4 pre-built for Hadoop 3](https://archive.apache.org/dist/spark/spark-3.4.4/spark-3.4.4-bin-hadoop3.tgz)
   - Extract it to a directory, e.g. `C:\Spark\spark-3.4.4-bin-hadoop3`
   - Set the `SPARK_HOME` environment variable:
     ```powershell
     $env:SPARK_HOME = "C:\\Spark\\spark-3.4.4-bin-hadoop3"
     ```

5. **(Optional) Remove the built-in Spark Python directory to avoid interpreter conflicts**  
   ⚠️ This step prevents PySpark from using the wrong Python version:
   ```powershell
   move C:\Spark\spark-3.4.4-bin-hadoop3\python C:\Spark\spark-3.4.4-bin-hadoop3\python_backup
   ```

6. **Set PySpark environment variables**  
   These commands tell PySpark which Python interpreter to use:
   ```powershell
   $env:PYSPARK_PYTHON = "C:\\Users\\Admin\\product_categories\\.venv_py310\\Scripts\\python.exe"
   $env:PYSPARK_DRIVER_PYTHON = "C:\\Users\\Admin\\product_categories\\.venv_py310\\Scripts\\python.exe"
   ```

## Running the Script

1. Make sure you're in the project directory:
   ```powershell
   cd C:\Users\Admin\product_categories
   ```

2. Run the script with Spark:
   ```powershell
   spark-submit --master local[1] test_spark.py
   ```

## Expected Output

The script performs the following:
- Displays the original DataFrame with names and ages.
- Filters the DataFrame to show only people older than 25.

Sample output:
```text
Original DataFrame:
+-----+---+
| Name|Age|
+-----+---+
|Alice| 25|
|  Bob| 30|
|Cathy| 28|
|David| 22|
+-----+---+

Filtered DataFrame (Age > 25):
+-----+---+
| Name|Age|
+-----+---+
|  Bob| 30|
|Cathy| 28|
+-----+---+
```

## Notes

- This script is designed to run in a **local Spark** environment.
- If you encounter `SocketTimeoutException`, temporarily **disable your firewall** or ensure Spark ports are allowed.