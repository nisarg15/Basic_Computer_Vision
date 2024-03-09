import numpy as np
from PIL import Image

image3 = Image.open("iribefront.jpg")
img = np.array(image3)

red = img[:,:,0]

green = img[:,:,1]

img[:,:,0] = green
img[:,:,1] = red
        
Im2 = Image.fromarray(np.uint8(img))
Im2.show()
