import requests

a = requests.get('https://raw.githubusercontent.com/w1n4a/CTkPlus/refs/heads/main/LICENSE')
print(a.text)
