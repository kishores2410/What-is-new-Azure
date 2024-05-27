import os 
from config import connection_string
from azure.data.tables import TableServiceClient

table_service_client = TableServiceClient.from_connection_string(connection_string)
table_client = table_service_client.get_table_client(table_name=os.getenv("TABLE_NAME"))