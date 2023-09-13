import requests

res = requests.get('https://api.chucknorris.io/jokes/random')
list = res.json()

print(list.get('value'))