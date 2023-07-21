import requests

url = 'https://www.google.co.jp/'
data = {'key1': 'value1'}
response = requests.put(url, data=data)