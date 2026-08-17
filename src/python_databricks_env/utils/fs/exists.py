from python_databricks_env.dbutils.Dbutils import Dbutils

dbutils = Dbutils()


def exists(path: str) -> bool:
    try:
        dbutils.fs.ls(path)
        return True
    except:
        return False
