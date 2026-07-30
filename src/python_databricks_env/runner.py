from python_databricks_env.dbutils.Dbutils import Dbutils

dbutils = Dbutils(widgets={"first": "1", "second": "2"})

dbutils.fs.cp(from_="/path/to/dir", to="/path/to/dest")

dbutils.widgets.get("first")
