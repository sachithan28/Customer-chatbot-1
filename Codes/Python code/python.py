import os
import google.generativeai as genai

# Set your API key here
API_KEY = "Your Api Key"

# Configure the Gemini API with the API key
genai.configure(api_key=API_KEY)

# Create the model with generation configurations
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(
    history=[
        # You can optionally add any initial messages here
    ]
)

def chatbot_response(user_input):
    # Send the user input to the chat session
    response = chat_session.send_message(user_input)
    return response.text

def main():
    print("Welcome to the Gemini Chatbot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        bot_message = chatbot_response(user_input)
        print(f"Bot: {bot_message}")

if __name__ == "__main__":
    main()
