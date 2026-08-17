import sys

from pyspark.sql.types import StructType, StructField, IntegerType


def test(spark):
    print("version:", sys.version)
    print("executable:", sys.executable)

    # df = spark.range(0, 10)
    df = spark.createDataFrame([(1,)], StructType([StructField("_1", IntegerType())]))

    df.show()
