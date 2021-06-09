import requests
import json

r = requests.get('http://127.0.0.1:5000/messages/')

print(r.text)
messages = r.json()

print(messages[0]["sender"])

print(type(messages))

