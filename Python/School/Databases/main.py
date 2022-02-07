import sqlite3
from sqlite3 import Error

# # Function to create a connection to the database
# def create_connection(path):
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print("Connection to DB successful")
#     except Error as e:
#         print(f"Error: '{e}'")

#     return connection

# # Creates a database
# def create_database(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Created a DB successfully")
#     except Error as e:
#         print(f"Error: '{e}'")

# connection = create_connection("db.sqlite")
# create_db_query = "CREATE DATABASE db_test"
# create_database(connection, create_db_query)

# Creating a DB
def db_create(connection, c, db_name):
    connection = sqlite3.connect('db.sqlite')
    c = connection.cursor()
    c.execute('''CREATE TABLE ''' + db_name + '''(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, number REAL)''')
    connection.commit()
    connection.close()

# Inserting Values
def insert_value(conn_insert, c_insert, db_name, name, number):
    conn_insert = sqlite3.connect('db.sqlite')
    c_insert = conn_insert.cursor()
    c_insert.execute("INSERT INTO " + db_name + " VALUES (?, ?)", (name, number))
    c_insert.commit()
    c_insert.close()

connection = sqlite3.connect("db.sqlite")
c = connection.cursor()

print(
"""
1. Create DB
2. Insert Value
"""
)
choice = int(input())
if choice == 1:
    database_name = input("Database name: ")
    db_create(connection, c, database_name)

elif choice == 2:
    database_name = input("Database name: ")
    name = input("Name: ")
    number = int(input("Number: "))
    insert_value(connection, c, database_name, name, number)