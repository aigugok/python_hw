#Загрузили функцию из прошлого дз, с помощью GPSPhoto вытащили из exif данных картинок ширину и долготу

from hw16 import gps_data_location_and_url
from GPSPhoto import gpsphoto

photos=['20210626_202821.jpg', 'IMG_4263.JPG','IMG_4833.JPG','IMG_5365.JPG']
for i in photos:
    data = gpsphoto.getGPSData(i)
    if data!=None:
        print(gps_data_location_and_url(f"{data['Latitude']},{data['Longitude']} \n"))


