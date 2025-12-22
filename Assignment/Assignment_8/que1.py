from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import streamlit as st
import os
import json
import requests

load_dotenv()

st.header("Agent")

@tool
def calculator(expression):
    """
    This calculator function solves any arithmetic expression containing all content values.
    It supports basic arithmetic operators +,-,*,/ and parenthesis.
    """
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error: Cannot solve expression"


@tool 
def get_weather(city):
    """
    This get_weather() function gets the current weather of given city.
    """
    try:
        api_key = os.getenv("weather_api")
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
        response = requests.get(url)
        weather = response.json()
        return json.dumps(weather)
    except:
        return "Error"


@tool
def read_file(filepath):
    """
    This function reads the content of a text file from the given file path
    and returns its content as a string.
    """
    with open(filepath, 'r') as file:
        text = file.read()
        return text



llm = init_chat_model(
    model="google/gemma-3-4b",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="non-needed"
)

agent = create_agent(
    model=llm,
    tools=[
        calculator,
        get_weather,
        read_file 
    ],
    system_prompt="You are a helpful assistant. Answer in short."
)

user_input = st.chat_input("You: ", key="chat_input")

if user_input:
    if user_input == "exit":
        st.stop()

    result = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })

    llm_output = result["messages"][-5]
    st.write("AI: ", llm_output.content)


