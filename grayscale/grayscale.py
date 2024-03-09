import numpy as np
from PIL import Image

image3 = Image.open("iribefront.jpg")
img = np.array(image3)

x = np.shape(img)

# Luminosity method
for i in x:
        red = img[:,:,0]
        green = img[:,:,1]
        blue = img[:,:,2]
        grayscale2 = (0.3*red + 0.11*blue + 0.59*green)
        
Im2 = Image.fromarray(np.uint8(grayscale2))
Im2.show()
