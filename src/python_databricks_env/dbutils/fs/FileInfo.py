from collections.abc import Callable
from pathlib import Path

from pyspark.sql import SparkSession

from python_databricks_env.utils.fs.is_dbfs import is_dbfs
from python_databricks_env.utils.fs.resolve import resolve


class FileInfo:

    def __init__(self, spark: SparkSession, path: str, dbfs: Callable[[SparkSession], bool] = is_dbfs):
        self._path = Path(path)

        self.path = resolve(spark, path, dbfs=dbfs)
        self.name = self._path.name
        self.size = self._path.stat().st_size if not self._path.is_dir() else 0
        self.modificationTime = self._path.stat().st_mtime

    def isDir(self) -> bool:
        return self._path.is_dir()

    def isFile(self) -> bool:
        return self._path.is_file()

    def __str__(self) -> str:
        path = f"path='{self.path}'"
        name = f"name='{self.name}'"
        size = f"size={self.size}"
        modificationTime = f"modificationTime={self.modificationTime}"
        return f"FileInfo({path}, {name}, {size}, {modificationTime})"
