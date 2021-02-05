from urllib import request, parse
import json
import os

url = 'https://api.thecatapi.com/v1/images/search'
path = '/Users/admin/VScode/Python/networkreq.py'

params = {
    'limit' : 5,
    'page' : 1,
    'order' : 'Desc'
}

querystring = parse.urlencode(params)

with request.urlopen(url + '?' + querystring) as response:
    content = response.read().decode('utf-8')

print(content)

with open("file.json", "w+") as file:
    file.write(content)

# In Json Format

# with request.urlopen(url) as response:
#     content = response.read()
    
# data = json.loads(content)

# print(data['status'])