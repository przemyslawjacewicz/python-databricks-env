from pyspark.sql import SparkSession

from python_databricks_env.utils.get_logger import get_logger

logger = get_logger(__name__)


def is_dbfs(spark: SparkSession | None) -> bool:
    if spark is None:
        return False
    else:
        try:
            return spark.sparkContext.getConf().get("spark.databricks.clusterUsageTags.clusterId") is not None
        except Exception as ex:
            logger.error(f"Error checking if on DBFS env: {ex}")
            return False
