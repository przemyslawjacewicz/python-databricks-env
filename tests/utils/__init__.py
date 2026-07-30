import os
import sys

from delta import configure_spark_with_delta_pip
from dotenv import load_dotenv
from pyspark.sql import SparkSession

load_dotenv()


def get_or_create_spark() -> SparkSession:
    # PYSPARK_PYTHON
    os.environ["PYSPARK_PYTHON"] = sys.executable
    print(f"{os.environ['PYSPARK_PYTHON']=}")

    # PYSPARK_DRIVER_PYTHON
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
    print(f"{os.environ['PYSPARK_DRIVER_PYTHON']=}")

    # JAVA_HOME
    if "JAVA_HOME" in os.environ:
        print(f"Using JAVA_HOME from environment: {os.environ['JAVA_HOME']}")
    else:
        print("WARNING: JAVA_HOME not found in .env or system environment.")
    print(f"{os.environ['JAVA_HOME']=}")

    builder = (
        SparkSession
        .builder
        .appName("spark-python-utils")
        .master("local[1]")

        # .config("spark.driver.host", "127.0.0.1")
        # .config("spark.driver.bindAddress", "127.0.0.1")

        .config("spark.sql.shuffle.partitions", "1")
        .config("spark.default.parallelism", "1")
        .config("spark.rdd.compress", "false")
        .config("spark.ui.enabled", "false")
        # .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true")
        # .config("spark.python.worker.faulthandler.enabled", "true")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    )

    return configure_spark_with_delta_pip(builder).getOrCreate()
