from urllib import request
import json

url = 'https://dog.ceo/api/breeds/list/all'

with request.urlopen(url) as response:
    content = response.read()
    
data = json.loads(content)

print(data['status'])