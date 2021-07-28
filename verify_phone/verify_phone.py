import phonenumbers

from phonenumbers import geocoder

PHONE = "+5511995000005"

phone_number = phonenumbers.parse(PHONE)

loc = geocoder.description_for_number(phone_number, 'pt')

print(loc)
