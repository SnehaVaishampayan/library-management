import sqlite3
import uuid
from datetime import datetime
import Constants
from Constants import CREATE_BOOK, status_list, user_company
from database.CreateDatabase import get_cursor, connect_to_db


# This function is responsible for getting the list of books assigned to the user's company.
def get_books_by_user_company(logged_in_username):
    print("In get_books ")
    books = []
    try:
        cur = get_cursor()
        query_filter = {'company': user_company[logged_in_username]}
        cur.execute(get_query(query_filter))
        rows = cur.fetchall()

        for i in rows:
            book = {}
            book["id"] = i["id"]
            book["name"] = i["name"]
            book["description"] = i["description"]
            book["created"] = i["created"]
            book["updated"] = i["updated"]
            book["status"] = i["status"]
            book["creator"] = i["creator"]
            book["company"] = i["company"]
            books.append(book)

    except Exception as e:
        print("Error occurred while getting BookModule details.", str(e))
        books = []
    return books


# This function is responsible for getting the list of books given the specific book details.
def get_books_by_filter(request_filter):
    print("In get_books_by_filter ")
    books = []
    try:
        if 'company' in request_filter.keys():
            get_books_by_user_company(request_filter.get('company'))
        else:
            query = get_query(request_filter)
            cur = get_cursor()
            cur.execute(query)
            rows = cur.fetchall()
            for i in rows:
                book = {}
                book["id"] = i["id"]
                book["name"] = i["name"]
                book["description"] = i["description"]
                book["created"] = i["created"]
                book["updated"] = i["updated"]
                book["status"] = i["status"]
                book["creator"] = i["creator"]
                book["company"] = i["company"]
                books.append(book)

    except Exception as e:
        print("Exception occurred while getting BookModule given ID. ", str(e))
        return books
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


# This function is responsible for validation of the request payload while creating Book.
def validate_book_payload(book_payload):
    print("In validate_book_payload")
    if len(book_payload) != 3:
        raise Exception("Book details are missing.")
    for each_data in book_payload:
        if each_data not in Constants.create_book_attributes:
            raise Exception("Incorrect data. Please provide Book Name, Book Description and Book Status")
    for each_data in book_payload:
        if each_data.lower() == 'name':
            if len(book_payload.get('name')) > 15:
                raise Exception("Book details validation failed. Too long Book Name.")

        if each_data.lower() == 'description':
            if len(book_payload.get('description')) > 150:
                raise Exception("Book details validation failed. Too long description.")

        if each_data.lower() == 'status':
            if book_payload.get('status').lower() not in status_list:
                raise Exception("Book details validation failed. Invalid Status")
    return True

# This function is responsible for creating the Book.
def create_book(book_payload, login_username):
    print("In create_book ")
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        if not validate_book_payload(book_payload):
            raise Exception("Book Validation failed.")

        book_payload['id'] = str(uuid.uuid4())
        book_payload['created'] = datetime.now()
        book_payload['updated'] = datetime.now()
        book_payload['creator'] = login_username
        book_payload['company'] = user_company[login_username]
        cur.execute(CREATE_BOOK, (
            book_payload['id'], book_payload['name'], book_payload['description'], book_payload['created'],
            book_payload['updated'], book_payload['status'], book_payload['creator'],
            book_payload['company']))
        conn.commit()

    except Exception as e:
        print("Exception while creating Book Module." + str(e))
        conn().rollback()

    finally:
        conn.close()
    return book_payload
