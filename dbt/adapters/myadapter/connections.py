import jaydebeapi
from dataclasses import dataclass

from dbt.adapters.base import Credentials
from dbt.adapters.sql import SQLConnectionManager
from dbt.adapters.base import Credentials
from dbt.logger import GLOBAL_LOGGER as logger


@dataclass
class MyAdapterCredentials(Credentials):
    # Add credentials members here, like:
    username: str
    password: int
    clientId: str
    clientSecret: str

    @property
    def type(self):
        return 'salesforce-cdp'

    def _connection_keys(self):
        # return an iterator of keys to pretty-print in 'dbt debug'.
        # Omit fields like 'password'!
        return ('username', 'clientId')


class SalesforceCDPAdapterConnectionManager():
    TYPE = 'salesforce-cdp'

    @classmethod
    def open(cls, connection):
        #if connection.state == 'open':
           # logger.debug('Connection is already open, skipping open.')
           # return connection

        ## credentials = cls.get_credentials(connection.credentials)
        ## print(credentials)

        try:
            properties = {
                'userName': '232e2e@cdp.org',
                'password': 'test1234',
                'clientId': '3MVG9SemV5D80oBcgWlgI8AZBNui7FDe1fAxwQh1xDxQ1fz6ClS5nbTKqNQSm9JjhNwfhf.1heAhDblREFIXJ',
                'clientSecret': '41E7B104BA06328F684FFC089313D35E4E77DABBAA7BF3813F2CAAF41C75BAE0'
            }

            conn = jaydebeapi.connect("com.salesforce.cdp.queryservice.QueryServiceDriver",
                                      "jdbc:queryService-jdbc:https://login.salesforce.com", properties,
                                      'queryService-jdbc-1.3-jar-with-dependencies.jar', )

            cur = conn.cursor()
            args = {}
            cur.execute('select ssot__Number__c from ssot__Account__dlm limit 10', args)
            one = cur.fetchall()
            print(one)
            conn.close()

            connection.state = 'open'
            connection.handle = conn
        except Exception as inst:
            print(inst)
            print('error making the connection object')
            # handle = myadapter_library.connect(
            #     host=credentials.host,
            #     port=credentials.port,
            #     username=credentials.username,
            #     password=credentials.password,
            #     catalog=credentials.database
            # )
            #connection.handle = None
            #connection.state = 'fail'
            #raise dbt.exceptions.FailedToConnectException('error making the connection object')
        return connection

    # @classmethod
    # def get_response(cls, cursor):
    #     return cursor.status_message

    #     def cancel(self, connection):
    #     tid = connection.handle.transaction_id()
    #     sql = 'select cancel_transaction({})'.format(tid)
    #     logger.debug("Cancelling query '{}' ({})".format(connection_name, pid))
    #     _, cursor = self.add_query(sql, 'master')
    #     res = cursor.fetchone()
    #     logger.debug("Canceled query '{}': {}".format(connection_name, res))

    # @contextmanager
    # def exception_handler(self, sql: str):
    #     try:
    #         yield
    #     except myadapter_library.DatabaseError as exc:
    #         self.release(connection_name)

    #         logger.debug('myadapter error: {}'.format(str(e)))
    #         raise dbt.exceptions.DatabaseException(str(exc))
    #     except Exception as exc:
    #         logger.debug("Error running SQL: {}".format(sql))
    #         logger.debug("Rolling back transaction.")
    #         self.release(connection_name)
    #         raise dbt.exceptions.RuntimeException(str(exc))


tmp = SalesforceCDPAdapterConnectionManager()
tmp.open(None)
