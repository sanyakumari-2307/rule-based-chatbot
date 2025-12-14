import re
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting responses
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello there! 👋 How can I help you today?"

    # Asking name
    elif re.search(r'\b(your name|who are you)\b', user_input):
        return "I'm a simple rule-based chatbot built using Python!"

    # How are you
    elif re.search(r'\b(how are you)\b', user_input):
        return "I'm just a bunch of code, but I’m doing great! How about you?"

    # Date and time
    elif re.search(r'\b(time|date)\b', user_input):
        now = datetime.now()
        return f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}"

    # Weather
    elif re.search(r'\b(weather)\b', user_input):
        return "I can’t check the weather right now, but I hope it's nice outside! ☀️"

    # Goodbye
    elif re.search(r'\b(bye|exit|quit)\b', user_input):
        return "Goodbye! 👋 Have a great day ahead!"

    # Default fallback
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("🤖 Rule-Based Chatbot (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if re.search(r'\b(bye|exit|quit)\b', user_input.lower()):
            break

if __name__ == "__main__":
    main()
