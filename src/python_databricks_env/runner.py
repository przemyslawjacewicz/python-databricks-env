from python_databricks_env.dbutils.DbUtils import DbUtils

dbutils = DbUtils(widgets={"first": "1", "second": "2"})

dbutils.fs.cp(source="/path/to/dir", dest="/path/to/dest")

dbutils.widgets.get("first")
