import os

import dotenv
import psycopg2


dotenv.load_dotenv()


try:
    conn = psycopg2.connect(
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="127.0.0.1",
        port=5432,
    )

    cursor = conn.cursor()

    # Check database connection
    cursor.execute("SELECT version();")
    version = cursor.fetchone()

    print("Connection established successfully!")
    print(f"PostgreSQL version: {version[0]}")

except psycopg2.Error as e:
    print("Failed to connect to PostgreSQL.")
    print(f"Error: {e}")

finally:
    if "cursor" in locals():
        cursor.close()

    if "conn" in locals():
        conn.close()

    print("Connection closed.")