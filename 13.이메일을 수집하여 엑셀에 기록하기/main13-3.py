import requests
import re

url = 'http://news.v.daum.net/v/20211129144552297'

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=ut-8'
    }

response = requests.get(url, headers=headers)

result = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)

result = list(set(result))

print(result)
