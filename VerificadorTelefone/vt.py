import phonenumbers
from phonenumbers import geocoder

phone = input("Digite o fone no formato +55DD99999999: ")

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))



