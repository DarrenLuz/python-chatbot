
import streamlit as st
import random

st.set_page_config(
    page_title="Python Chatbot",
    page_icon="🤖"
)

st.title("🤖 My Python Chatbot")
st.write("Hello! I am your chatbot. Ask me something.")


def get_response(user_message):
    message = user_message.lower().strip()

    if any(word in message.split() for word in ["hi", "hello", "hey"]):
        return random.choice([
            "Hello! How are you?",
            "Hi there! How can I help?",
            "Hey! Nice to meet you."
        ])

    elif "your name" in message or "who are you" in message:
        return "I am a Python chatbot built using Streamlit."

    elif "python" in message:
        return (
            "Python is a high-level programming language "
            "used in web development, automation, and AI."
        )

    elif "how are you" in message:
        return "I am doing great! Thanks for asking."

    elif "thank" in message:
        return "You're welcome!"

    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a great day."

    return (
        "Sorry, I don't understand that yet. "
        "Try asking me about Python."
    )


# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! How can I help you today?"
        }
    ]

# Display existing messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Receive user input and respond
prompt = st.chat_input("Type your message here...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    response = get_response(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()

# Clear conversation
if st.button("Clear chat"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Chat cleared! What would you like to ask?"
        }
    ]
    st.rerun()
