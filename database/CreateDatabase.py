import sqlite3
import uuid
from datetime import datetime

from Constants import DROP_TABLE, CREATE_TABLE_QUERY, CREATE_BOOK_QUERY

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
        conn.execute(CREATE_TABLE_QUERY)
        init_book_1 = {}
        init_book_1['id'] = str(uuid.uuid4())
        init_book_1['created'] = datetime.now()
        init_book_1['updated'] = datetime.now()
        conn.execute(CREATE_BOOK_QUERY, (
            init_book_1['id'], 'test_book_name_1',
            'test_description_1', init_book_1['created'],
            init_book_1['updated'], "to do", 'test_author_1',
            'test_publication_1','10'))
        init_book_2 = {}
        init_book_2['id'] = str(uuid.uuid4())
        init_book_2['created'] = datetime.now()
        init_book_2['updated'] = datetime.now()
        conn.execute(CREATE_BOOK_QUERY, (
            init_book_2['id'], 'test_book_name_2',
            'test_description_2', init_book_2['created'],
            init_book_2['updated'], "to do", 'test_author_2',
            'test_publication_2','10'))

        conn.commit()
        print("Book table created successfully")
        conn.close()
    except Exception as e:
        print("Book table creation failed.", str(e))


# This function is responsible for passing the cursor to execute queries other functions.
def get_cursor():
    print("In cursor")
    conn = sqlite3.connect('./database/database.db')
    conn.row_factory = sqlite3.Row
    return conn.cursor()
