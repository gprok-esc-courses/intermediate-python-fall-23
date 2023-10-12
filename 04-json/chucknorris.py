import requests
import json

response = requests.get('https://api.chucknorris.io/jokes/random')
print(response.text)

joke = json.loads(response.text)
print(joke['value'])

