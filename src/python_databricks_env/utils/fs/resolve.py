import re
from collections.abc import Callable

from pyspark.sql import SparkSession

from python_databricks_env.utils.fs.is_dbfs import is_dbfs


def resolve(*parts: str, dbfs: Callable[[SparkSession], bool] = is_dbfs) -> str:
    _spark = SparkSession.getActiveSession()

    if _spark is not None:
        raw = "/".join(parts)
        normalized = re.sub(r"/+", "/", raw).rstrip("/")

        if dbfs(_spark):
            return f"dbfs:{normalized}" if not normalized.startswith("dbfs:") else normalized
        else:
            return normalized
    else:
        raise Exception("SparkSession is not available")
