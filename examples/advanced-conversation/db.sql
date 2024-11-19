-- Create the users table
CREATE TABLE advanced_conversation_users (
    id INT AUTO_INCREMENT PRIMARY KEY
);

-- Create the messages table
CREATE TABLE advanced_conversation_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    user_id INT,
    type ENUM('system', 'human', 'ai') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES advanced_conversation_users(id) ON DELETE CASCADE
);
