import requests

try:
    url="https://nilesh-g.github.io/learn-web/data/novels.json"
    response= requests.get(url)
    print("status_code=", response.status_code)
    print("text:",response.text)
    data=response.json()
    print("Response Data: ",data)

except:
    print("Error Occured!")