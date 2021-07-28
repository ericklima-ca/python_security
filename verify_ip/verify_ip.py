import re, json
from urllib.request import urlopen

URL = 'https://ipinfo.io/json'

response = urlopen(URL)

data = json.load(response)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print(ip, org, city, country, region, sep='\n')
