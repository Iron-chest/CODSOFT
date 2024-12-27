# Simple Chatbot Project

## Overview
This project implements a simple rule-based chatbot using Python. The chatbot responds to user inputs based on predefined rules, showcasing fundamental concepts in natural language processing and conversation flow.

---

## Features
- **Rule-Based Responses:** Utilizes a dictionary to map user inputs to predefined responses.
- **Case-Insensitive Matching:** Normalizes user inputs to ensure robust matching.
- **Interactive Chat Session:** Allows users to interact with the chatbot in a conversational manner.
- **Graceful Exit:** Users can type `bye` to terminate the chat session.

---

## Class and Method Details

### 1. **Class Definition**
```python
class SimpleChatbot:
```
This class encapsulates the chatbot’s functionality, promoting code organization and reusability.

### 2. **Initialization Method**
```python
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "how are you": "I'm just a computer program, but thanks for asking! How can I help you?",
            "what is your name": "I am a simple chatbot created to assist you.",
            "bye": "Goodbye! Have a great day!",
        }
```
- **Purpose:** Initializes the chatbot with predefined responses stored in a dictionary.
- **Key Attribute:** `self.responses` – Maps user inputs (keys) to chatbot responses (values).

### 3. **Response Retrieval Method**
```python
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "I'm sorry, I don't understand that. Can you ask something else?"
```
- **Normalization:** Converts input to lowercase and trims whitespace for consistent processing.
- **Logic:** Checks if the input exists in the `self.responses` dictionary; returns the corresponding value or a default message.

### 4. **Chat Loop Method**
```python
    def start_chat(self):
        print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print(self.get_response(user_input))
                break
            response = self.get_response(user_input)
            print("Bot:", response)
```
- **Purpose:** Initiates and manages the interactive chat session.
- **Exit Condition:** Ends the loop if the user types `bye`.

### 5. **Main Program Execution**
```python
if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.start_chat()
```
- **Main Check:** Ensures the script runs only when executed directly.
- **Instance Creation:** Instantiates the `SimpleChatbot` class.
- **Chat Start:** Invokes the `start_chat` method to begin the conversation.

---

## Usage
1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```bash
    cd simple-chatbot
    ```

3. Run the chatbot script:
    ```bash
    python chatbot.py
    ```

4. Interact with the chatbot by typing inputs in the terminal.

---

## Example Conversation
```
Welcome to the Simple Chatbot! Type 'bye' to exit.
You: hello
Bot: Hi there! How can I assist you today?
You: how are you
Bot: I'm just a computer program, but thanks for asking! How can I help you?
You: bye
Bot: Goodbye! Have a great day!
```

---

## Learning Outcomes
- Understanding of class-based programming in Python.
- Implementation of rule-based responses using dictionaries.
- Hands-on experience with input normalization and response matching.
- Familiarity with Python’s interactive console programming.

---

## Contributions
Contributions are welcome! Feel free to fork the repository, make enhancements, and submit a pull request.


