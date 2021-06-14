from dbt.adapters.sql import SQLAdapter
from dbt.adapters.myadapter import MyAdapterConnectionManager


class MyAdapterAdapter(SQLAdapter):
    ConnectionManager = MyAdapterConnectionManager
