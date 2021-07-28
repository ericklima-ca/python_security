from bs4 import BeautifulSoup
import requests as req

site = req.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/25').content

soup = BeautifulSoup(site, 'html.parser')

cidade = soup.find('h1', class_="-bold -font-18 -dark-blue _margin-r-10 _margin-b-sm-5").text
temp_min = soup.find(id='min-temp-1')
temp_max = soup.find(id='max-temp-1')
print(cidade, temp_min.string, temp_max.string)
