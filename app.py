#!/usr/bin/python

from flask import Flask, request, jsonify
from flask_cors import CORS
from LoginModule.LoginHandler import is_user_authenticated
from database.DatabaseHandler import database_handler
from BookModule import BookHandler
from LoginModule.LoginHandler import is_user_admin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# An API endpoint to o create a BookModule
@app.route('/api/book/add', methods=['POST'])
def api_add_book():
    response_books = []
    response = {}
    try:
        if not is_user_authenticated(request.authorization):
            response_books = 'Invalid user'
            raise Exception
        elif not is_user_admin(request.authorization['username']):
            print("in app")
            response_books = 'Only admins can add the book to the library'
            raise Exception
        else:
            response = BookHandler.create_book_service(request.get_json(), request.authorization['username'])
            print(response)
            return jsonify(response)

    except:
        response['status'] = 400
        response['message'] = response_books
        return jsonify(response)


# An API endpoint to get details about a specific BookModule
@app.route('/api/books', methods=['GET'])
def api_get_all_books():
    response = []
    if is_user_authenticated(request.authorization):
        if len(request.args) == 0:
            all_books_list = BookHandler.get_all_books()
        else:
            all_books_list = BookHandler.get_books_by_filter(request.args)
        return jsonify(all_books_list)
    else:
        response.append("Invalid user")
    return jsonify(response)


# An API endpoint to o update a Book
@app.route('/api/book/update', methods=['PUT'])
def api_update_book():
    response_books = []
    response = {}
    try:
        if not is_user_authenticated(request.authorization):
            response_books = 'Invalid user'
            raise Exception
        elif not is_user_admin(request.authorization['username']):
            print("in app")
            response_books = 'Only admins can update the book from the library'
            raise Exception
        else:
            response = BookHandler.update_book(request.get_json(), request.authorization['username'])
            print(response)
            return jsonify(response)
    except:
        response['status'] = 400
        response['message'] = response_books
        return jsonify(response)


# This function is responsible for starting the application
if __name__ == '__main__':
    print('In main app.py ')
    database_handler()
    app.config['JSON_SORT_KEYS'] = False
    app.run()
