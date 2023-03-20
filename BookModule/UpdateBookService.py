import sqlite3
from datetime import datetime
import Constants
from BookModule.validate_book_payload import validate_book_payload
from LoginModule.LoginHandler import is_user_admin
from database.CreateDatabase import connect_to_db


# This function is responsible for updating the Book.
def update_book(book_payload, login_username):
    global conn
    print("In update_book ")
    if not is_user_admin(login_username):
        raise Exception("Only admins can update the book details.")
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        if not validate_book_payload(book_payload):
            raise Exception("Book Validation failed.")

        book_payload['updated'] = datetime.now()
        cur.execute(Constants.UPDATE_BOOK_QUERY, (book_payload['name'], book_payload['updated'], book_payload['id']))
        conn.commit()

    except Exception as e:
        print("Exception while creating Book Module." + str(e))
        conn().rollback()

    finally:
        conn.close()
    return book_payload
