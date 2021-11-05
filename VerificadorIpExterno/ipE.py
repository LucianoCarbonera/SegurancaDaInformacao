import re  #Permite operações com expressões regulares
import json
from urllib.request import urlopen  #Funções e classe que ajudam abrir URls

url = 'https://ipinfo.io/json'

reposta = urlopen(url)

dados = json.load(reposta)

ip = dados['ip']
org = dados['org']
city = dados['city']

print("Detalhes IP externo")
print(f'IP: {ip}\nCidade: {city}')



