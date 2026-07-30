from python_databricks_env.utils.fs.resolve import resolve
from utils import get_or_create_spark

spark = get_or_create_spark()


def test_resolve_local():
    assert resolve(spark, "/path/to/file", dbfs=lambda _: False) == "/path/to/file"
    assert resolve(spark, "/path/to/file/", dbfs=lambda _: False) == "/path/to/file"

    assert resolve(spark, "/path/", "/to/", "/file/", dbfs=lambda _: False) == "/path/to/file"
    assert resolve(spark, "/path", "to", "file", dbfs=lambda _: False) == "/path/to/file"

    assert resolve(spark, "path/to/file", dbfs=lambda _: False) == "path/to/file"
    assert resolve(spark, "path/to/file/", dbfs=lambda _: False) == "path/to/file"

    assert resolve(spark, "path/", "/to/", "/file/", dbfs=lambda _: False) == "path/to/file"
    assert resolve(spark, "path", "to", "file", dbfs=lambda _: False) == "path/to/file"


def test_resolve_dbfs():
    assert resolve(spark, "/path/to/file", dbfs=lambda _: True) == "dbfs:/path/to/file"
    assert resolve(spark, "/path/to/file/", dbfs=lambda _: True) == "dbfs:/path/to/file"

    assert resolve(spark, "/path/", "/to/", "/file/", dbfs=lambda _: True) == "dbfs:/path/to/file"
    assert resolve(spark, "/path", "to", "file", dbfs=lambda _: True) == "dbfs:/path/to/file"

    assert resolve(spark, "path/to/file", dbfs=lambda _: True) == "dbfs:path/to/file"
    assert resolve(spark, "path/to/file/", dbfs=lambda _: True) == "dbfs:path/to/file"

    assert resolve(spark, "path/", "/to/", "/file/", dbfs=lambda _: True) == "dbfs:path/to/file"
    assert resolve(spark, "path", "to", "file", dbfs=lambda _: True) == "dbfs:path/to/file"
