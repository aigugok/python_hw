#С помощью бибилиотеки geopy можно узнать местоположение по ширине и долготе (сервис Nominatim),url для Goggle Maps сформирован "в лоб" c помощью f-string
from geopy.geocoders import Nominatim
import requests
geolocator = Nominatim(user_agent="myapp")


def gps_data_location_and_url(gps_data):
    try:
        geolocator.reverse(gps_data)
    except ValueError:
        return f"Not allowed format of GPS data"
    location = geolocator.reverse(gps_data)
    return f"Location: {location.address}\nGoggle Maps URL: https://www.google.com/maps/search/?api=1&query={gps_data}"



def gps_data_from_file(filename):
    with open(filename,"r") as f:
        for line in f:
            line=line.replace(",",".").split(";")
            for i in range(len(line)):
                degres=line[i].split(".")[0]
                line[i]=line[i].replace(degres+".","")
                minutes=line[i].split("'")[0]
                line[i]= str((int(minutes)/60) + int(degres))
            print(gps_data_location_and_url(",".join(line)))


#запуск программы
# gps_data_from_file("gps_data.txt")

