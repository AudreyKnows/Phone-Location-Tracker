import phonenumbers 
from test import number 

from phonenumbers import geocoder 
Ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(Ch_nmber, "en" ))

from phonenumbers import carrier 
Service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(Service_nmber, " en"))