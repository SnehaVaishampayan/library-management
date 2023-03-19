CREATE_TABLE_QUERY = "CREATE TABLE Book ( id TEXT PRIMARY KEY NOT NULL, name TEXT NOT NULL, " \
                     "description TEXT NOT NULL,created TEXT NOT NULL,updated TEXT NOT NULL," \
                     "status TEXT NOT NULL,author TEXT NOT NULL,publication TEXT NOT NULL, copies INTEGER NOT NULL)"

CREATE_BOOK_QUERY = "INSERT INTO Book (id, name, description, created, updated, status, author, publication, copies) " \
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

UPDATE_BOOK_QUERY = "UPDATE Book SET name= ?, updated = ? WHERE id = ?"

GET_ALL_BOOKS = "SELECT * FROM Book"
DROP_TABLE = "DROP TABLE IF EXISTS Book"

GET_BOOK_BY_ID = "SELECT * FROM Book WHERE id = ?"

book_attributes = ["id", "name", "description", "created", "updated", "status", "author", "publication", "copies"]
create_book_attributes = ["id", "name", "description", "status", "author", "publication", "copies"]

status_list = ["to do", "in progress", "finished", "closed"]
authenticated_users = {"admin": "admin", "user1": "password1", "user2": "password2",
                       "user3": "password3", "user4": "password4", "user5": "password5"}
admin_list = ["admin"]
user_company = {"user1": "company1", "user2": "company2", "user3": "company3", "user4": "company4", "user5": "company5"}
