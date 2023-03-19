
# This function is responsible for validation of the request payload while creating Book.
import Constants


def validate_book_payload(book_payload):
    print("In validate_book_payload")
    if len(book_payload) < 3:
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
            if book_payload.get('status').lower() not in Constants.status_list:
                raise Exception("Book details validation failed. Invalid Status")
    return True
