from dbt.adapters.myadapter.connections import MyAdapterConnectionManager
from dbt.adapters.myadapter.connections import MyAdapterCredentials
from dbt.adapters.myadapter.impl import MyAdapterAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import myadapter


Plugin = AdapterPlugin(
    adapter=MyAdapterAdapter,
    credentials=MyAdapterCredentials,
    include_path=myadapter.PACKAGE_PATH)
