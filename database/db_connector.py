# db_connector.py
import mysql.connector
from sqlalchemy import create_engine


class DatabaseConnector:
    def __init__(self, host, user, port, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        self.engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")

    def execute_query(self, query, params=None):
        self.cursor = self.connection.cursor()

        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query):
        self.cursor = self.connection.cursor()

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()

    def get_engine(self):
        return self.engine
