class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "how are you": "I'm just a chatbot, but thanks for asking! How can I help you?",
            "what is your name": "I am a simple chatbot created to assist you.",
            "bye": "Goodbye! Have a great day!",
        }

    def get_response(self, user_input):
        # Normalize user input to lowercase for consistent matching
        user_input = user_input.lower().strip()
        
        # Check for predefined responses
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "I'm sorry, I don't understand that. Can you ask something else?"

    def start_chat(self):
        print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print(self.get_response(user_input))
                break
            response = self.get_response(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.start_chat()
