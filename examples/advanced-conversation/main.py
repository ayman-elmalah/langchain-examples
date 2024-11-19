import sys
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from db.messages import fetch_messages_from_db, save_message_to_db
from db.users import get_or_create_user
from core.messages import system_message_content, welcome_message

load_dotenv()

# Initialize the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Get the user_id from the command-line arguments
if len(sys.argv) < 2:
    print("Please provide your user id, {id}")
    sys.exit(1)

user_id = int(sys.argv[1])

# Ensure the user exists in the database or create the user if it doesn't
user_id = get_or_create_user(user_id)

# Fetch existing messages from the database or use defaults if empty
messages = fetch_messages_from_db(user_id)

# If no messages are found, start with system and welcome messages
if not messages:
    messages = [
        SystemMessage(content=system_message_content),
        AIMessage(content=welcome_message)
    ]
    # Save the system and welcome messages to the database
    save_message_to_db(system_message_content, 'system', user_id)
    save_message_to_db(welcome_message, 'ai', user_id)

# Print the initial welcome message if it exists
print(f"Elmalah Coffee: {welcome_message}")

while True:
    # Get input from the user
    user_input = input("You: ")

    # Check if the user wants to exit
    if user_input.lower() == "exit":
        print("Elmalah Coffee: Thank you for visiting! Have a great day! ☕️😊")
        break

    # Attach the user's message to the conversation
    human_message = HumanMessage(content=user_input)
    messages.append(human_message)
    # Save the human message to the database
    save_message_to_db(user_input, 'human', user_id)

    # Get the response from the AI model
    result = model.invoke(messages)

    # Attach the AI's response to the conversation
    ai_message = AIMessage(content=result.content)
    messages.append(ai_message)
    # Save the AI response to the database
    save_message_to_db(result.content, 'ai', user_id)

    # Print the AI's response
    print(f"Elmalah Coffee: {result.content}")
