# 1. Implement the chunking examples discussed in the provided PDF document.
# *Optional Question*

# Create a Streamlit web application that allows users to connect to a 
# MySQL database and ask natural language questions. 
# The app should generate and execute SELECT SQL queries using an LLM 
# and display both the query results and a simple English explanation.
# Note:
# Use the sample MySQL connection parameters provided in connection.txt 
# and the sample database schema in db.txt for testing.
# pip install mysql-connector-python

import streamlit as st
from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs = text_splitter.create_documents(["Gen Ai is leading area in IT sector , it replace humans but create new opportunity"])
st.write(docs)
print(docs)