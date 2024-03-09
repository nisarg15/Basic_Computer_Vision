import numpy as np
from PIL import Image

image3 = Image.open("iribefront.jpg")
img = np.array(image3)

# Average method
x = np.shape(img)

for i in x:
        red = img[:,:,0]
        green = img[:,:,1]
        blue = img[:,:,2]
        red = np.float64(red)
        green = np.float64(green)
        blue = np.float64(blue)
        grayscale = (red + blue + green) /3
    
Im = Image.fromarray(np.uint8(grayscale))
Im.show()
