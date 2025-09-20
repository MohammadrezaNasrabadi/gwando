import psycopg2
from psycopg2 import sql
import os


from custom_logger import get_custom_logger


logger = get_custom_logger(__name__)


database_host = os.getenv('DATABASE_HOST', 'postgres')
database_name = os.getenv('DATABASE_NAME', 'gandoo')
database_user = os.getenv('DATABASE_USER', 'postgres')
database_password = os.getenv('DATABASE_PASSWORD', 'password')


class DatabaseConnection:
    _connection = None

    @staticmethod
    def get_connection():
        if DatabaseConnection._connection is None:
            DatabaseConnection._connection = psycopg2.connect(
                dbname=database_name,
                user=database_user,
                password=database_password,
                host=database_host,
            )
            logger.info("connected to database successfully.")
        return DatabaseConnection._connection

    @staticmethod
    def close_connection():
        if DatabaseConnection._connection:
            DatabaseConnection._connection.close()
            DatabaseConnection._connection = None
            logger.info("database connection closed.")

