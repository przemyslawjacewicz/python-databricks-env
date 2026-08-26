from python_databricks_env.dbutils.DbUtils import DbUtils
from python_databricks_env.utils.get_logger import get_logger

dbutils = DbUtils()

logger = get_logger(__name__)


def exists(path: str) -> bool:
    try:
        dbutils.fs.ls(path)
        return True
    except Exception as ex:
        logger.error(f"Error while checking if path exists: {ex}")
        return False
