import psycopg2
from queries import queries
from os import getenv
import logging as log

if __name__ == "__main__":
    db_connection = None
    try:
        # Make a connection to the database
        db_connection = psycopg2.connect(database = getenv("APP_DB_NAME"),
                                    user = getenv("APP_DB_USER"),
                                    password = getenv("APP_DB_USER_PASSWORD"),
                                    host = getenv("APP_DB_HOST"),
                                    port = getenv("APP_DB_PORT"))

        # A transaction: rollbacks if there is an error. Autocommits by default if everything goes OK.
        with db_connection:
            # Not a real database cursor unless a parameter is passed.
            # It is used to send queries to the database and get the results
            with db_connection.cursor() as cursor:
                cursor.execute(queries["create_users_table"])
                cursor.execute(queries["insert_user"], {'name': 'username'})
                cursor.execute(queries["get_users"])
                
                print("Fetched results: ")
                for register in cursor:
                    print(register)
    except:
        log.exception("An exception has been thrown. The program will terminate now")
    finally:
        if db_connection != None and not db_connection.closed:
            db_connection.close()