def chatbot():
    print("Welcome to the basic chatbot! (type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break  # exit the loop and end the chatbot
        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
