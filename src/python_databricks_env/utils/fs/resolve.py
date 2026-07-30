import re
from collections.abc import Callable

from pyspark.sql import SparkSession

from python_databricks_env.utils.fs.is_dbfs import is_dbfs


def resolve(spark: SparkSession, *parts: str, dbfs: Callable[[SparkSession], bool] = is_dbfs) -> str:
    raw = "/".join(parts)
    normalized = re.sub(r"/+", "/", raw).rstrip("/")

    if dbfs(spark):
        return f"dbfs:{normalized}" if not normalized.startswith("dbfs:") else normalized
    else:
        return normalized
