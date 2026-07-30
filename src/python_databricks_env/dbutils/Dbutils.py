from python_databricks_env.dbutils.fs.Fs import Fs
from python_databricks_env.dbutils.notebook.Notebook import Notebook
from python_databricks_env.dbutils.widgets.Widgets import Widgets


class Dbutils:

    def __init__(self, widgets=None):
        if widgets is None:
            widgets = {}
        self.fs = Fs()
        self.notebook = Notebook()
        self.widgets = Widgets(widgets)
