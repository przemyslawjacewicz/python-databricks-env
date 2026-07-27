# def exists(path: str) -> bool:
#     try:
#         dbutils.fs.ls(path)
#         return True
#     except:
#         return False
from pyspark.sql import SparkSession


# def walk_files[T](dir: str, func: Callable[[str], T]) -> list[T]:
# get parent
# _dbutils._fs.ls(dir)
# root = Path(dir)
#
# if not root.is_dir():
#     raise NotADirectoryError(f"Not a directory: {root}")
#
# results: list[T] = []
#
# for path in root.iterdir():
#     if path.is_file():
#         results.append(func(path))
#     elif path.is_dir():
#         results.extend(walk_files_recursive(path, func))
#
# return results

# def is_dbfs(spark: SparkSession) -> bool:
#     return spark.sparkContext.getConf().get("spark._databricks.clusterUsageTags.clusterId") is not None

def resolve(spark: SparkSession, *parts: str) -> str:
    print(f"{spark.sparkContext.getConf().get("spark._databricks.clusterUsageTags.clusterId")=}")
    start = "dbfs:/" if not parts[0].startswith("dbfs:") else ""
    return start + "/".join([part.strip("/") for part in parts])
