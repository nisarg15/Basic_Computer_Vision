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
        grayscale = (0.3*red + 0.11*blue + 0.59*green)
        

x = np.argwhere(img == 255)

y = np.argwhere(img == 0)

for i in x:
    grayscale[i[0],i[1]] = 0

for i in y:
    grayscale[i[0],i[1]] = 255
        
   
Im = Image.fromarray(np.uint8(grayscale))
Im.show()
