import numpy as np
from PIL import Image
from copy import deepcopy

image3 = Image.open("iribefront.jpg")
img = np.array(image3)

x = np.shape(img)

img_2 = np.zeros(((x[0]),(x[1])))
red_img = deepcopy(img_2)
green_img = deepcopy(img_2)
blue_img = deepcopy(img_2)

red = img[:,:,0]

green = img[:,:,1]

blue = img[:,:,2]

red_intensity = np.argwhere(red > 127)
green_intensity = np.argwhere(green > 127)
blue_intensity = np.argwhere(blue > 127)

for i in red_intensity:
    red_img[i[0],i[1]] = 255
for i in green_intensity:
    green_img[i[0],i[1]] = 255
for i in blue_intensity:
    blue_img[i[0],i[1]] = 255

average_red = np.mean(red_img)
average_green = np.mean(green_img)
average_blue = np.mean(blue_img)

print("Red channel average is " ,average_red)
print("Green channel average is ", average_green)
print("Blue channel average is ", average_blue)
