





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

