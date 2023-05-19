from swagger_server.resources.postgres_db import PostgresClient

class ItemRepository():

    def create(self, body):
        response = None
        with PostgresClient() as client:
            response = client.execute_insert('"ITEM"',body)
        return response 
    
    def get_by_id(self, item_id):
        response = None
        with PostgresClient() as client:
            response = client.execute_query('SELECT * FROM "ITEM" WHERE ID=' + str(item_id))
            return response
        
    def update(self, body, item_id):
        response = None
        with PostgresClient() as client:
            response = client.execute_update('"ITEM"', body,'id = ' + str(item_id))
        return response
        
    def get_paginated(self, page, size, name):
        response = None
        with PostgresClient() as client:
            table = '"ITEM"'
            query = f"SELECT * FROM {table} WHERE name like '%{name}%'"
            response = client.execute_query_paginated(query, page, size)
        return response
        
