import itertools
import requests

# importing geopy library
from geopy.geocoders import Nominatim

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# entering the location name




addresses = [
    "Empire State Building, New York City",
    "Statue of Liberty, New York City",
    "Central Park, New York City",
    "One World Trade Center, New York City",
    "Brooklyn Bridge, New York City"
]

lst = []

for addr in addresses:
    getLoc = loc.geocode(addr)
    dct = {"Addr":addr, "Lat": getLoc.latitude, "Lon": getLoc.longitude}
    lst.append(dct)



print(lst[0])
print(lst[0]["Lat"])

