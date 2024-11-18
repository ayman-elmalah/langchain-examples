from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from db.connection import get_db_connection

# Function to fetch messages from the database based on user_id
def fetch_messages_from_db(user_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Query to get messages for a specific user
    query = """
        SELECT content, type FROM advanced_conversation_messages 
        WHERE user_id = %s ORDER BY created_at ASC
    """
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()

    # Close the database connection
    cursor.close()
    connection.close()

    # Parse messages into the correct format
    messages = []
    for row in rows:
        content = row['content']
        message_type = row['type']

        if message_type == 'system':
            messages.append(SystemMessage(content=content))
        elif message_type == 'human':
            messages.append(HumanMessage(content=content))
        elif message_type == 'ai':
            messages.append(AIMessage(content=content))

    return messages

# Function to save a message to the database
def save_message_to_db(content, message_type, user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Query to insert a new message
    query = """
        INSERT INTO advanced_conversation_messages (content, type, user_id) 
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (content, message_type, user_id))
    connection.commit()

    # Close the database connection
    cursor.close()
    connection.close()
