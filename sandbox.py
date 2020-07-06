
from PIL import Image
from multiprocessing import Pool
from math import sqrt, pow


image = Image.open('paracord.jpg')


def to_perceived_brightness(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    perceived_brightness_v1 = int(0.299*r + 0.587*g + 0.114*b)
    perceived_brightness_v2 = int(
        sqrt(0.299*(r**2) + 0.587*(g**2) + 0.114*(b**2))
    )
    return (perceived_brightness_v2, 0, 0)


pixels = list(image.getdata())
pixels_perceived_brightness = list(map(to_perceived_brightness, pixels))
image.putdata(pixels_perceived_brightness)
image.show()