import sqlite3
import uuid
from datetime import datetime

from flask import jsonify

import Constants
from BookModule.validate_book_payload import validate_book_payload
from Constants import CREATE_BOOK_QUERY, status_list, user_company
from database.CreateDatabase import get_cursor, connect_to_db
from LoginModule.LoginHandler import is_user_admin


# This function is responsible for getting the list of all the books.
def get_all_books():
    print("In get_all_books ")
    books = []
    try:
        cur = get_cursor()
        # query_filter = {'company': user_company[logged_in_username]}
        # cur.execute(get_query(query_filter))
        cur.execute(Constants.GET_ALL_BOOKS)
        rows = cur.fetchall()
        print("rows len ", len(rows))
        for i in rows:
            book = {"id": i["id"], "name": i["name"], "description": i["description"], "created": i["created"],
                    "updated": i["updated"], "status": i["status"], "author": i["author"],
                    "publication": i["publication"], "copies": i["copies"]}
            books.append(book)
    except Exception as e:
        print("Error occurred while getting BookModule details.", str(e))
        books = []
    return books


# This function is responsible for getting the list of books assigned to the user's company.
def get_books_by_author(filter_attribute, filter_value):
    print("In get_books ")
    books = []
    try:
        cur = get_cursor()
        query_filter = ''
        if filter_attribute == 'author':
            query_filter = {'author': query_filter}
        cur.execute(get_query(query_filter))
        rows = cur.fetchall()
        print("fa ", len(rows))
        for i in rows:
            book = {"id": i["id"], "name": i["name"], "description": i["description"], "created": i["created"],
                    "updated": i["updated"], "status": i["status"], "creator": i["creator"], "company": i["company"]}
            books.append(book)

    except Exception as e:
        print("Error occurred while getting BookModule details.", str(e))
        books = []
        return books


# This function is responsible for getting the list of books given the specific book details.
def get_books_by_filter(request_filter):
    print("In get_books_by_filter ", request_filter)
    books = []
    try:
        if 'author' in request_filter.keys():
            get_books_by_author('author',request_filter.get('author'))
        else:
            query = get_query(request_filter)
            cur = get_cursor()
            cur.execute(query)
            rows = cur.fetchall()
            for i in rows:
                book = {"id": i["id"], "name": i["name"], "description": i["description"], "created": i["created"],
                        "updated": i["updated"], "status": i["status"], "creator": i["creator"],
                        "company": i["company"]}
                books.append(book)

    except Exception as e:
        print("Exception occurred while getting BookModule given ID. ", str(e))
        # return books
    return books


# This function is responsible for building the query from the provided filters.
def get_query(filters):
    print("In get_query")
    query = Constants.GET_ALL_BOOKS + " where "
    conditions = ""
    for eachFilterKey in filters.keys():
        if conditions == "":
            conditions += eachFilterKey + "=" + "'" + filters.get(eachFilterKey) + "'"
        else:
            conditions += " and " + eachFilterKey + "=" + "'" + filters.get(eachFilterKey) + "'"
    return query + "" + conditions


# This function is responsible for creating the Book.
def create_book(book_payload, login_username):
    global conn
    print("In create_book ")
    response = {}
    response['status'] = 200
    # response['message'] = response_books
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
        response['message'] = (book_payload)
        conn.commit()

    except Exception as e:
        print("Exception while creating Book Module." + str(e))
        conn().rollback()
        response['status'] = 400
        response['message'] = "Exception while creating Book Module." + str(e)
    finally:
        conn.close()
    return response


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

        # book_payload['id'] = str(uuid.uuid4())
        book_payload['created'] = datetime.now()
        book_payload['updated'] = datetime.now()
        cur.execute(Constants.CREATE_BOOK_QUERY, (
            book_payload['id'], book_payload['name'],
            book_payload['description'], book_payload['created'],
            book_payload['updated'], book_payload['status'],
            book_payload['author'],
            book_payload['publication'],
            book_payload['copies']))
        conn.commit()

    except Exception as e:
        print("Exception while creating Book Module." + str(e))
        conn().rollback()

    finally:
        conn.close()
    return book_payload
