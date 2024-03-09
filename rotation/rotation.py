import numpy as np
from PIL import Image

image3 = Image.open("iribefront.jpg")
img = np.array(image3)

x = np.shape(img)


img_crop = img[int(x[0]/2):int(x[0]/2) + 372,int(x[1]/2):int(x[1]/2) + 372]

image_90 = np.rot90(img_crop)
image_180 = np.rot90(img_crop,2)
image_270 = np.rot90(img_crop,3)

final_image = np.concatenate((image_90,image_180,image_270),axis = 1)
        
Im2 = Image.fromarray(np.uint8(final_image))
Im2.show()
