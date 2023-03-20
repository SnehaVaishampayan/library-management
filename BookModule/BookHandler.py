from BookModule.CreateBookHandler import create_book
from BookModule.UpdateBookService import update_book
from BookModule.GetBooksService import get_all_books,get_books_by_filter


# This function is responsible for getting the list of all the books.
def get_all_books_service():
    return get_all_books()


# This function is responsible for creating the Book.
def create_book_service(book_payload, login_username):
    return create_book(book_payload, login_username)


# This function is responsible for updating the Book.
def update_book_service(book_payload, login_username):
    return update_book(book_payload, login_username)


# This function is responsible for getting the list of books given the specific book details.
def get_books_by_filter_service(request_filter):
    return get_books_by_filter(request_filter)
