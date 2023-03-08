CREATE_TABLE = "CREATE TABLE Book ( id TEXT PRIMARY KEY NOT NULL, name TEXT NOT NULL, " \
                     "description TEXT NOT NULL,created TEXT NOT NULL,updated TEXT NOT NULL," \
                     "status TEXT NOT NULL,creator TEXT NOT NULL,company TEXT NOT NULL)"

CREATE_BOOK = "INSERT INTO Book (id, name, description, created, updated, status, creator, company) " \
                 "VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

GET_ALL_BOOKS = "SELECT * FROM Book"
DROP_TABLE = "DROP TABLE IF EXISTS Book"

GET_BOOK_BY_ID = "SELECT * FROM Book WHERE id = ?"

book_attributes = ["id", "name", "description", "created", "updated", "status", "creator", "company"]
create_book_attributes = ["name", "description", "status"]

status_list = ["to do", "in progress", "finished", "closed"]
authenticated_users = { "user1": "password1", "user2":"password2","user3":"password3", "user4": "password4", "user5": "password5"}
user_company = { "user1":"company1", "user2":"company2","user3":"company3", "user4":"company4", "user5":"company5" }