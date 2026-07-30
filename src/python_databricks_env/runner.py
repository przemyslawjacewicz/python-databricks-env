from python_databricks_env.dbutils.Dbutils import Dbutils

dbutils = Dbutils(widgets={"first": "1", "second": "2"})

dbutils.fs.cp(source="/path/to/dir", dest="/path/to/dest")

dbutils.widgets.get("first")
