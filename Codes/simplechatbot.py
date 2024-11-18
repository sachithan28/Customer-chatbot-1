import random
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.data import find

try:
    find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Sample responses for different intents
responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Hey! How's it going?"
    ],
    "goodbye": [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Bye! Hope to talk again soon!"
    ],
    "thank_you": [
        "You're welcome!",
        "No problem at all!",
        "Happy to help!"
    ],
    "weather": [
        "It's sunny outside!",
        "It looks like it might rain today.",
        "Expect cloudy weather."
    ],
    "unknown": [
        "I'm sorry, I don't understand that.",
        "Could you please clarify?",
        "I'm not sure I follow. Can you rephrase?"
    ]
}

# Simple intent recognition using keywords
def identify_intent(user_input):
    tokens = word_tokenize(user_input.lower())

    # Define keywords for each intent
    greeting_keywords = ["hello", "hi", "hey", "greetings"]
    goodbye_keywords = ["bye", "goodbye", "see you", "farewell"]
    thank_you_keywords = ["thank you", "thanks", "appreciate"]
    weather_keywords = ["weather", "rain", "sunny", "forecast"]

    # Check for intent based on keywords
    if any(word in tokens for word in greeting_keywords):
        return "greeting"
    elif any(word in tokens for word in goodbye_keywords):
        return "goodbye"
    elif any(word in tokens for word in thank_you_keywords):
        return "thank_you"
    elif any(word in tokens for word in weather_keywords):
        return "weather"
    else:
        return "unknown"

# Response generation function
def generate_response(intent):
    return random.choice(responses[intent])

# Main chat function
def chatbot():
    print("Chatbot: Hello! I'm here to help. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break

        # Identify intent and generate response
        intent = identify_intent(user_input)
        response = generate_response(intent)
        print("Chatbot:", response)

# Run the chatbot
chatbot()
