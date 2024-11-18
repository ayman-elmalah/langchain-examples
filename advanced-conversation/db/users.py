from db.connection import get_db_connection

# Function to check if a user exists in the database, create if not
def get_or_create_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Check if the user exists
    query = "SELECT id FROM advanced_conversation_users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()

    if user is None:
        # If user doesn't exist, create a new user
        cursor.execute("INSERT INTO advanced_conversation_users (id) VALUES (%s)", (user_id,))
        connection.commit()

    # Close the database connection
    cursor.close()
    connection.close()

    return user_id
