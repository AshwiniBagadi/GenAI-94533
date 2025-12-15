# 1. Upload a CSV file. Input a SQL query from user and execute it on the CSV
# data (as dataframe ). Display result on the

import streamlit as st
import pandas as pd

st.header("DATAFRAME")

file=st.file_uploader("Upload a CSV file: ", type="csv")

if file:
    df=pd.read_csv(file)
    st.dataframe(df)