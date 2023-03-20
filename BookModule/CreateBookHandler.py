import sqlite3
import uuid
from datetime import datetime
from BookModule.validate_book_payload import validate_book_payload
from Constants import CREATE_BOOK_QUERY
from LoginModule.LoginHandler import is_user_admin
from database.CreateDatabase import connect_to_db


# This function is responsible for creating the Book.
def create_book(book_payload, login_username):
    global conn
    print("In create_book ")
    response = {'status': 200}
    try:
        if not is_user_admin(login_username):
            print("not admin")
            raise Exception("Only admins can add new book.")
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        if not validate_book_payload(book_payload):
            raise Exception("Book Validation failed.")

        book_payload['id'] = str(uuid.uuid4())
        book_payload['created'] = datetime.now()
        book_payload['updated'] = datetime.now()
        cur.execute(CREATE_BOOK_QUERY, (
            book_payload['id'], book_payload['name'],
            book_payload['description'], book_payload['created'],
            book_payload['updated'], book_payload['status'],
            book_payload['author'],
            book_payload['publication'],
            book_payload['copies']))
        print(book_payload)
        response['message'] = book_payload
        conn.commit()

    except Exception as e:
        print("Exception while creating Book Module." + str(e))
        conn().rollback()
        response['status'] = 400
        response['message'] = "Exception while creating Book Module." + str(e)
    finally:
        conn.close()
    return response
