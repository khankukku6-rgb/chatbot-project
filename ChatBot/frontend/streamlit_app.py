import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="Simple Chatbot", page_icon="💬")

st.title("💬 Simple Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(
                BACKEND_URL,
                json={"prompt": user_input},
                timeout=60
            )

            if response.status_code == 200:
                reply = response.json()["response"]
            else:
                reply = "⚠️ Backend error"

            st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
