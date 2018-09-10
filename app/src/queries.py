# Database queries
queries = {
    "create_users_table": """
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL
        ); 
    """,
    "insert_user": """
        INSERT INTO Users (name)
        VALUES ( %(name)s );
    """,
    "get_users": """
        SELECT *
        FROM Users;
    """
}