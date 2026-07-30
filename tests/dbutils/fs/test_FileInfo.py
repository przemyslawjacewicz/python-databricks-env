import time

from python_databricks_env.dbutils.fs.FileInfo import FileInfo
from utils import get_or_create_spark

spark = get_or_create_spark()


def test_FileInfo_dir(tmp_path):
    start = time.time()
    time.sleep(1)

    dir = tmp_path / "dir"
    dir.mkdir(parents=True, exist_ok=True)

    time.sleep(1)

    fi = FileInfo(spark, str(dir), lambda _: False)

    assert fi.path == str(dir)
    assert fi.name == "dir"
    assert fi.size == 0
    assert start < fi.modificationTime
    assert fi.modificationTime < time.time()
    assert fi.isDir()
    assert not fi.isFile()


def test_FileInfo_file(tmp_path):
    start = time.time()
    time.sleep(1)

    file = tmp_path / "file"
    # file.touch(exist_ok=True)
    with open(file, "w") as f:
        f.write("Hello, world!")

    time.sleep(1)

    fi = FileInfo(spark, str(file), lambda _: False)

    assert fi.path == str(file)
    assert fi.name == "file"
    assert fi.size > 0
    assert start < fi.modificationTime
    assert fi.modificationTime < time.time()
    assert not fi.isDir()
    assert fi.isFile()
