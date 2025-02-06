import psycopg2
import os

# PostgreSQL connection URL from Render
DATABASE_URL = "postgresql://my_poll_app_db_user:omGvoatPyrOvjKdj49Ggucv6LZiNsJz8@dpg-cuigbld6l47c73af4p40-a.oregon-postgres.render.com/my_poll_app_db"

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variable
db_url = os.getenv("DATABASE_URL")
print("Database URL:", db_url)

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ Successfully connected to PostgreSQL!")

    # Create a cursor
    cursor = conn.cursor()

    # Test the connection (optional)
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Database Version:", db_version)

    # Close connection
    cursor.close()
    conn.close()
    print("🔒 Connection closed.")

except Exception as e:
    print("❌ Connection failed:", e)
