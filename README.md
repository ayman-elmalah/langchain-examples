# Langchain Examples Documentation

This repository contains examples for using Langchain in various projects. The examples demonstrate how to interact with AI models and integrate them into conversations with simple to advanced setups.

## Table of Contents

1. [Installation](#1-installation)
2. [Directory Structure](#2-directory-structure)
3. [Examples](#3-examples)
    1. [chat-models](#chat-models)
    2. [basic-conversation](#basic-conversation)
    3. [advanced-conversation](#advanced-conversation)


## 1. Installation

To get started with the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/ayman-elmalah/langchain-examples
    ```

2. Navigate to the project folder:

    ```bash
    cd langchain-examples
    ```

3. Copy the `.env.example` file to `.env`:

    ```bash
    cp .env.example .env
    ```

4. Add the necessary environment variables in the `.env` file (e.g., API keys for OpenAI, etc.).

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## 2. Directory Structure

The repository is organized into multiple directories based on the different projects. Below is the structure:

```plaintext
langchain-examples/
├── .env.example
├── .env
├── requirements.txt
├── chat-models/
│   └── main.py
├── basic-conversation/
│   └── main.py
├── advanced-conversation/
│   ├── db/
│   │   ├── connection.py
│   │   ├── messages.py
│   │   └── users.py
│   ├── core/
│   │   ├── messages.py
│   ├── db.sql
│   └── main.py
```

## 3. Examples

This repository contains three projects, each demonstrating a different aspect of working with Langchain.

### chat-models

This is a very basic implementation where the user sends a message to the AI model, and the model responds.

- **How it works**: The user sends a single message, and the AI model processes the message and returns a response.
- **To run it**: Simply run the following command:

    ```bash
    python3 chat-models/main.py
    ```

### basic-conversation

This project demonstrates a basic conversation with the AI. It includes a system message and a human message.

- **How it works**: The model is initialized, and a predefined set of messages is sent to the model, including a system message and a human query. The AI responds with an answer.
- **To run it**: To execute the basic conversation example, run the following command:

    ```bash
    python3 basic-conversation/main.py
    ```

### advanced-conversation

This project builds on the previous ones by adding more complex functionality, such as storing and fetching messages from a MySQL database.

- **How it works**: The system interacts with a MySQL database to store and retrieve conversation history. You can send and receive messages, and the AI model will respond based on the previous conversation.
- **Database setup**: You need to create a MySQL database and import the provided SQL schema (`db.sql`).

    1. Create a database in MySQL (e.g., `ai_langchain_test`).
    2. Import the `db.sql` file to set up the necessary tables.
    3. Update your `.env` file with the database connection credentials.

- **To run it**: After setting up the database, run the following command:

    ```bash
    python3 advanced-conversation/main.py 1
    ```
