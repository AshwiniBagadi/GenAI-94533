import os
import requests
import json
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("CHATBOT")

if "model" not in st.session_state:
    st.session_state.model = "home"


def home():
    st.subheader("AI using Groq and Local LLM")
    if st.button("GROQ", type="primary"):
        st.session_state.model= "groq"
    if st.button("LOCAL", type="primary"):
        st.session_state.model= "local"


def groq_ai():
    st.subheader("GROQ Based AI")
    api_key1 = os.getenv("groq_api")

    url = "https://api.groq.com/openai/v1/chat/completions"

    if "message" not in st.session_state:
        st.session_state.message= []

    user_input= st.chat_input("Ask Anything..")

    if user_input and user_input != "exit":
        headers= {
            "Authorization": f"Bearer {api_key1}",
            "Content-Type": "application/json"
        }

        req_data= {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "user", "content": user_input}
            ],
        }

        response= requests.post(url, data=json.dumps(req_data), headers=headers)
        resp= response.json()

        output= resp["choices"][0]["message"]["content"]

        st.session_state.message.append(user_input)
        st.session_state.message.append(output)

    # Display chat history
    for idx, msg in enumerate(st.session_state.message):
        role = "user" if idx % 2 == 0 else "assistant"
        with st.chat_message(role):
            st.write(msg)


def local_ai():
    api_key2= "dummy-key"
    url= "http://127.0.0.1:1234/v1/chat/completions"

    headers= {
        "Authorization": f"Bearer {api_key2}",
        "Content-Type": "application/json"
    }

    if "messages" not in st.session_state:
        st.session_state.messages= []

    user_prompt = st.chat_input("Ask anything: ")

    if user_prompt and user_prompt!= "exit":
        req_data= {
            "model": "google/gemma-3-4b",
            "messages": [
                {"role": "user", "content": user_prompt}
            ],
        }

        response= requests.post(url, data=json.dumps(req_data), headers=headers)
        resp= response.json()

        output= resp["choices"][0]["message"]["content"]

        st.session_state.messages.append(user_prompt)
        st.session_state.messages.append(output)

    # Display chat history
    for idx, message in enumerate(st.session_state.messages):
        role= "user" if idx % 2==0 else "assistant"
        with st.chat_message(role):
            st.write(message)


with st.sidebar:
    st.header("Models")
    groq= st.button("GROQ AI", type="primary")
    local= st.button("Local AI", type="primary")

    if groq:
        st.session_state.model= "groq"
    if local:
        st.session_state.model= "local"


if st.session_state.model== "home":
    home()
elif st.session_state.model== "groq":
    groq_ai()
elif st.session_state.model== "local":
    local_ai()
