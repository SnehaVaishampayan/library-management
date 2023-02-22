from database.CreateDatabase import create_db_table


# This function is responsible for creating the database and populating the test data.
def database_handler():
    print("In database_handler")
    create_db_table()
