from langchain.chat_models import init_chat_model
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("groq_api")
)
conversation = [
    {"role": "system", "content": "You are SQLite expert developer with 10 years of experience."}
]

csv_file=input("Enter path of csv file: ")
df=pd.read_csv(csv_file)

print("CSV Schema: ")
print(df.dtypes)

while True:
    user_input= input("Ask Anything about this CSV: ")
    if user_input=="exit":
        break
    llm_input=f"""
        Table Name: data
        Table Schema: {df.dtypes}
        Question: {user_input}
        Instructions:
            Write a SQL query for the above question.
            Generate SQL query only in plain text format and nothing else.
            If you can not generate the query, then output 'Error'.
    """
    result=llm.invoke(llm_input)
    print(result.content)
