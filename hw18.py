#Написать программу, которая будет создавать миниатюры фотографий. С помощью модуля Image библиотеки PIL можно изменить размер фотографии, сохраняем под новым именем.
from PIL import Image

def image_resizing(image_name, percent_from_old_size):
    try:
        foo = Image.open(image_name)
    except FileNotFoundError:
        return "This file doesn't exists"
    x, y = foo.size
    foo = foo.resize((int(x*percent_from_old_size),int(y*percent_from_old_size)),Image.ANTIALIAS)
    new_image_name="resized by "+str(int(percent_from_old_size*100))+"% "+image_name
    foo.save(new_image_name)
    return f"New photo saved as {new_image_name}"



photos=['20210626_202821.jpg', 'IMG_4263.JPG','IMG_4833.JPG','IMG_5365.JPG']
for i in range(len(photos)):
    print(image_resizing(photos[i],(i+1)/10))