import sqlite3

from Constants import DROP_TABLE, CREATE_TABLE

global conn


# This function is responsible for creating the database and establishing the connection.
def connect_to_db():
    conn = sqlite3.connect('./database/database.db')
    return conn


# This function is responsible for creating the table
def create_db_table():
    global conn
    print("In create_db_table")
    try:
        conn = sqlite3.connect(r"./database/database.db")
        conn.execute(DROP_TABLE)
        conn.execute(CREATE_TABLE)
        conn.commit()
        print("Project table created successfully")
        conn.close()
    except Exception as e:
        print("Project table creation failed.", str(e))


# This function is responsible for passing the cursor to execute queries other functions.
def get_cursor():
    print("In cursor")
    conn = sqlite3.connect('./database/database.db')
    conn.row_factory = sqlite3.Row
    return conn.cursor()
