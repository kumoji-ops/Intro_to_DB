#!/usr/bin/env python3
"""Creates a MySQL database without using SELECT or SHOW"""
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password'
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    cursor.close()
    connection.close()

except Error as e:
    print(f"Error: {e}")
