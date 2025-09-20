from custom_logger import get_custom_logger
from .connect_db import DatabaseConnection
from healthcheck.healthcheck import HealthCheck


logger = get_custom_logger(__name__)


def create_db():
    try:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS records (
            id SERIAL PRIMARY KEY,
            url VARCHAR,
            included_urls TEXT[],
            status_code INTEGER
        );
        """

        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
    except Exception as e:
        logger.error("failed to create table.")
        HealthCheck.set_status(False)
        connection.rollback()
        raise e
