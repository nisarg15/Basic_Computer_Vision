import numpy as np
from PIL import Image

image3 = Image.open("iribefront.jpg")
img = np.array(image3)

red = img[:,:,0]

green = img[:,:,1]

blue = img[:,:,2]

img = np.concatenate((red,green,blue), axis=0)
        
Im2 = Image.fromarray(np.uint8(img))
Im2.show()
