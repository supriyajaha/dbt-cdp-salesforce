from dbt.adapters.sql import SQLAdapter
from dbt.adapters.myadapter.connections import DbtCdpAdapterConnectionManager


class DbtCdpAdapter(SQLAdapter):
    ConnectionManager = DbtCdpAdapterConnectionManager

    @classmethod
    def date_function(cls):
        return 'CURRENT_DATE'
