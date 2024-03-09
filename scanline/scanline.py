import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image3 = Image.open("iribefront.jpg")
img = np.array(image3)

red = img[:,:,0]

green = img[:,:,1]

blue = img[:,:,2]

shape = np.shape(img)

x = list(range(1,int(shape[1])+1))
y_red = (red[250])
y_green = (green[250])
y_blue = (blue[250])


plt.plot([x],[y_red],'ro')
plt.plot([x],[y_green],'go')
plt.plot([x],[y_blue],'bo')
plt.show()
