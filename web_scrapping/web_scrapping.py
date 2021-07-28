from bs4 import BeautifulSoup
import requests as req

site = req.get('https://climatempo.com.br').content

soup = BeautifulSoup(site, 'html.parser')

temp = soup.prettify()

print(temp)
