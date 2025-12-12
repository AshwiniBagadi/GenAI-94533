# Exercise 3: Fetch data from JSONPlaceholder API and save to a file

import requests

url="https://jsonplaceholder.typicode.com/users"
resp=requests.get(url)
print("Status code: ",resp.status_code)
data=resp.json()
print("Text: ",resp.text)