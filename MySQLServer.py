import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust credentials if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',         # Replace with your username
            password='password'  # Replace with your password
        )

        if connection.is_connected():
            try:
                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error while creating database: {e}")
            finally:
                cursor.close()

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
