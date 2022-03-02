import requests

url = 'https://www.wikipedia.org/'

response = requests.get(url, verify=True)

print('Status code', response)