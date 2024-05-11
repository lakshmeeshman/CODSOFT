#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# Define responses for different types of user inputs
responses = {
    "greetings": ["Hey there!", "Hello!", "Hi!", "Hey, how's it going?"],
    "how_are_you": ["I'm feeling groovy!", "I'm doing great, thanks for asking!",
                    "I'm fabulous, thanks for checking in!"],
    "weather": ["Looks like a perfect day to stay indoors and chat!",
                "I'm not a meteorologist, but it's always sunny in my world!"],
    "jokes": ["Why was the math book sad? Because it had too many problems!",
              "What do you call fake spaghetti? An impasta!",
              "Why don't skeletons fight each other? They don't have the guts!"],
    "farewell": ["Goodbye! Catch you later!", "See you later, alligator!", "Adios!", "Bye-bye!"],
    "default": ["Hmmm... I'm not sure what you mean. Let's chat about something else!",
                "I'm still learning, can you ask me something else?"]
}


# Function to generate chatbot response based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()

    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        return random.choice(responses["greetings"])
    elif "how are you" in user_input:
        return random.choice(responses["how_are_you"])
    elif "weather" in user_input:
        return random.choice(responses["weather"])
    elif "joke" in user_input:
        return random.choice(responses["jokes"])
    elif any(bye_word in user_input for bye_word in ["bye", "goodbye", "see you"]):
        return random.choice(responses["farewell"])
    else:
        return random.choice(responses["default"])


# Main function to interact with the chatbot
def main():
    print("Welcome to the Amusing Chatbot!")
    print("Feel free to chat with me. If you want to exit, just say 'bye' or 'goodbye'.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if any(bye_word in user_input for bye_word in ["bye", "goodbye", "see you"]):
            break


if __name__ == "__main__":
    main()




# In[ ]:




