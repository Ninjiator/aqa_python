import pathlib
import psycopg2
import pytest
import os


@pytest.fixture(scope="session")
def conn():
    connection = psycopg2.connect(
        host = os.getenv("POSTGRES_HOST"),
        port = os.getenv("POSTGRES_PORT"),
        dbname = os.getenv("POSTGRES_DB"),
        user = os.getenv("POSTGRES_USER"),
        password = os.getenv("POSTGRES_PASSWORD")
    )
    yield connection
    connection.close()


@pytest.fixture(scope="session", autouse=True)
def apply_db_schema(conn):
    schema_path = pathlib.Path(__file__).resolve().parents[1] / "db_schema.sql"
    sql = schema_path.read_text(encoding="utf-8")

    with conn.cursor() as cur:
        cur.execute(sql)
        conn.commit()

@pytest.fixture(autouse=True)
def clean_users_data(conn):
    with conn.cursor() as cur:
        cur.execute("TRUNCATE TABLE users RESTART IDENTITY;")
        conn.commit()


