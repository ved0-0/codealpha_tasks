def get_bot_response(user_message):
    message = user_message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi!"

    elif message in ["how are you", "how are you doing?"]:
        return "I'm fine, thanks!"

    elif message in ["what is your name?", "who are you?"]:
        return "I'm a simple rule-based chatbot."

    elif message in ["bye", "goodbye", "quit", "exit"]:
        return "Goodbye!"

    else:
        return "I'm not sure how to respond to that."


def start_chat():
    print("Chatbot started. Type 'bye' to exit.")
    print("-" * 30)

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)

        print("Bot:", response)

        if response == "Goodbye!":
            break


if __name__ == "__main__":
    start_chat()