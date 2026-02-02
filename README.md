# 🧠 Gemini Chatbot (Session-Memory Based)

A simple full-stack chatbot built using **FastAPI**, **Gemini**, and **Streamlit**, where **conversation memory is maintained only for the current UI session**.

The backend is completely **stateless**.
All conversational context is stored and replayed from the frontend for each request.

---

## ✨ Features

* 🔹 Gemini-powered conversational AI
* 🔹 Session-based memory (per browser session)
* 🔹 Stateless FastAPI backend
* 🔹 Clean separation between frontend and backend
* 🔹 System prompt loaded from external Markdown file
* 🔹 Fast, minimal UI using Streamlit

---

## 🧠 How Memory Works

This chatbot **does not store memory on the server or in a database**.

Instead:

1. Streamlit stores the chat history in `st.session_state`
2. On each user message, the **entire conversation history is sent again** to the backend
3. The backend prepends a system prompt and forwards the full context to Gemini
4. Gemini generates a response based on the provided context

> 💡 LLMs do not have persistent memory — memory is created by re-sending context.

Memory is:

* ✅ Preserved during the current UI session
* ❌ Lost on page refresh or browser restart

---

## 🏗️ Architecture Overview

```
Streamlit (Frontend)
  └── Stores conversation in session_state
  └── Sends full chat history on each request

FastAPI (Backend)
  └── Stateless
  └── Loads system prompt
  └── Forwards prompt to Gemini

Gemini API
  └── Generates response from provided text context
```

---

## 📁 Project Structure

```
project/
├── app/
│   ├── main.py              # FastAPI app
│   └── gemini/
│       └── gemini.py        # Gemini client
├── frontend/
│   └── streamlit_app.py     # Streamlit UI
├── system_prompt.md         # System instructions
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd project
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Set your Gemini API key:

```bash
export GOOGLE_API_KEY=your_api_key_here
```

On Windows (PowerShell):

```powershell
setx GOOGLE_API_KEY "your_api_key_here"
```

---

## ▶️ Running the Application

### Start the backend (FastAPI)

```bash
uvicorn app.main:app --reload
```

Backend runs at:
📍 `http://localhost:8000`

---

### Start the frontend (Streamlit)

```bash
streamlit run frontend/streamlit_app.py
```

Frontend runs at:
📍 `http://localhost:8501`

---

## 🧪 Example Interaction

```
User: What is JWT?
Assistant: JWT is a compact token used for authentication...

User: Do you remember my previous question?
Assistant: Yes — you asked about JWT earlier.
```

(The model “remembers” because the previous messages are included in the prompt.)

---

## 🚫 What This Project Does NOT Do (Yet)

* ❌ No database or long-term memory
* ❌ No user authentication
* ❌ No multi-user session persistence
* ❌ No token-limit management
* ❌ No streaming responses

---

## 🚀 Possible Future Improvements

* Conversation summarization to handle long chats
* Token-aware context trimming
* Persistent memory using a database
* Streaming responses
* Multiple system prompt profiles
* User authentication & session persistence

---

## 🧑‍💻 Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **LLM:** Google Gemini
* **Language:** Python 3

---

## 📌 Key Takeaway

> This project demonstrates how conversational memory can be implemented **without storing state on the server**, by replaying context from the frontend on every request.
