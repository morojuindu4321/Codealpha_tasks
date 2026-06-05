def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower().strip()

        if user in ["hello", "hi"]:
            print("🤖 Chatbot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("🤖 Chatbot: I am doing great. Thanks for asking!")

        elif user == "what is your name":
            print("🤖 Chatbot: My name is CodeAlpha Chatbot.")

        elif user == "who created you":
            print("🤖 Chatbot: I was created using Python.")

        elif user == "what can you do":
            print("🤖 Chatbot: I can answer simple predefined questions.")

        elif user == "tell me a joke":
            print("🤖 Chatbot: Why do programmers prefer dark mode? Because light attracts bugs!")

        elif user == "what is python":
            print("🤖 Chatbot: Python is a popular programming language.")

        elif user in ["thanks", "thank you"]:
            print("🤖 Chatbot: You're welcome!")

        elif user == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day.")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()