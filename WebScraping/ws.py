from bs4 import BeautifulSoup as bs
import requests

site = requests.get("https://climatempo.com.br").content

soup = bs(site, 'html.parser')
#print(soup.prettify())
#EXEMPLO
temp = soup.find("div", class_="col-md-2 col-6 _margin-t-sm-60")
print(temp.a)


