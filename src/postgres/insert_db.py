from psycopg2 import sql
from .connect_db import DatabaseConnection
from .schema import Data


from custom_logger import get_custom_logger


logger = get_custom_logger(__name__)


async def insert_db(data: Data):
    try:
        query = sql.SQL("""
        INSERT INTO records (url, included_urls, status_code)
        VALUES (%s, %s, %s)
        """)

        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (data.url, data.included_urls, data.status_code))
        connection.commit()
    except Exception as e:
        connection.rollback()
        logger.warn("failed to insert record to database.")
