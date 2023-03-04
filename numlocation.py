
#Finds the country

import phonenumbers
import folium
from mynumber import number
from phonenumbers import geocoder

Key = "32b8a6d8689a4f07aa2029778549bdf3"

samnumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samnumber, "en")
print(yourLocation)

# get the service provider name

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

#Finding the latititude and longitude for exact location

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']

long = results[0]['geometry']['lng']
print(lat, long)

myMap = folium.Map(location =[lat,long], zoom_start= 9)
folium.Marker([lat,long], popup= yourLocation).add_to((myMap)) 

#save map in html file

myMap.save("myLocation.html")   

