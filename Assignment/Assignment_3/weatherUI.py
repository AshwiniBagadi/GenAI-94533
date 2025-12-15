# 2. Show Login Form. If login is successful (fake auth if username & passwd is
# same, consider valid user), show weather page. There input a city name
# from text box and display current weather information. Provide a logout
# button and on its click, display thanks message.

import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv() 
api_key=os.getenv("weather_api")
st.title("WEATHER")

if "page" not in st.session_state:
    st.session_state.page = 'login page'

if "login" not in st.session_state:
    st.session_state.login=False

def login_page():
    st.subheader("Login")
    with st.form("User Details"):
        username=st.text_input("Enter Username")
        password=st.text_input("Enter password", type="password")
        login=st.form_submit_button("Login", type='primary')
        if login:
            if username == password and username!="":
                st.session_state.page="weather page"
                st.session_state.login=True
                st.toast("Login successful!")
            else:
                st.session_state.login=False
                st.session_state.page="login page"
                st.toast("No username and password!")

def weather_page():
        if st.session_state.login==True:
            st.subheader("Check Weather based on City")
            city=st.text_input("Enter City name ")
            
            if st.button("Search",type="primary"):
                try:
                    url= f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
                    resp=requests.get(url)
                    weather=resp.json()
                    st.write("Temperature: ",weather['main']['temp'])
                    st.write("Humidity: ",weather["main"]["humidity"])
                    st.write("Wind speed: ",weather["wind"]["speed"])
                except:
                    st.write("Invalid Input city details!")

        elif st.session_state.login==False:
            st.toast("Login First")
            if st.button("Login"):
                st.session_state.page="login page"
        
def logout_page():
    st.write("Thank you for using Weather App!")
    if st.button("Login again"):
        st.session_state.page="login page"

with st.sidebar:
    if st.button("Login", width="stretch"):
        st.session_state.page="login page"
    if st.button("check weather", width="stretch"):
        if st.session_state.login==True:
            st.session_state.page="weather page"
    if st.button("Log Out", width="stretch"):
        st.toast("Thank you!")
        st.session_state.login=False
        st.session_state.page="login page"
            


if st.session_state.page=="login page":
    login_page()
elif st.session_state.page=="weather page":
    weather_page()
elif st.session_state.page=="logout":
    logout_page()


