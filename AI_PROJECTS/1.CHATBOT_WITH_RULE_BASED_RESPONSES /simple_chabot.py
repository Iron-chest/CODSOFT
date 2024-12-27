class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I assist you today?",
            "hi": "Hi there! What can I do for you?",
            "how are you": "I'm just a program, but thanks for asking! How about you?",
            "what is your name": "I am a simple chatbot created to help you.",
            "bye": "Goodbye! Have a great day!",
            "help": "Sure! You can ask me about my functions or just say 'bye' to exit."
        }

    def get_response(self, user_input):
        # Normalize input to lower case for easier matching
        normalized_input = user_input.lower().strip()
        
        # Check for responses based on predefined rules
        if normalized_input in self.responses:
            return self.responses[normalized_input]
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def run(self):
        print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower().strip() == 'bye':
                print(self.get_response(user_input))
                break
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.run()
