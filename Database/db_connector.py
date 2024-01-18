# db_connector.py
import psycopg2

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()