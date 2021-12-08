import requests


value = input("Enter the value you want to convert:").strip(",")
# Where USD is the base currency you want to use
url = 'http://api.exchangeratesapi.io/v1/convert?access_key=678c3ab3339cb4283137428e6a3a5991&from=INR&to=USD' + '&amount=' + value

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)

# API key 678c3ab3339cb4283137428e6a3a5991
# http://api.exchangeratesapi.io/v1/latest?access_key=678c3ab3339cb4283137428e6a3a5991