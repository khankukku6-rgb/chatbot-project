import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("💬 Gemini Chatbot")

# ----------------------------
# Session memory (UI ONLY)
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Helper: build prompt from history
# ----------------------------

def build_prompt(messages):
    prompt = ""
    for msg in messages:
        role = msg["role"].capitalize()
        prompt += f"{role}: {msg['content']}\n"
    return prompt

# ----------------------------
# Render chat history
# ----------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------------------------
# User input
# ----------------------------

user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Build FULL conversation context
    conversation_prompt = build_prompt(st.session_state.messages)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(
                BACKEND_URL,
                json={"prompt": conversation_prompt},
                timeout=60
            )

            if response.status_code == 200:
                reply = response.json()["response"]
            else:
                reply = "⚠️ Backend error"

            st.markdown(reply)

    # Save assistant reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
