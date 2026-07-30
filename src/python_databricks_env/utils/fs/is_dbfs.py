from pyspark.sql import SparkSession


def is_dbfs(spark: SparkSession) -> bool:
    try:
        return spark.sparkContext.getConf().get("spark.databricks.clusterUsageTags.clusterId") is not None
    except:
        return False
