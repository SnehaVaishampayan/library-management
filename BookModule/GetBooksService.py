import Constants
from database.CreateDatabase import get_cursor


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
            get_books_by_author('author', request_filter.get('author'))
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