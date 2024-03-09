import numpy as np
from PIL import Image

image3 = Image.open("iribefront.jpg")
img = np.array(image3)
index_array = []

x = np.shape(img)


new_img = np.zeros((x[0],x[1]))

for y in x:
        red = img[:,:,0]
        green = img[:,:,1]
        blue = img[:,:,2]
        grayscale = (0.3*red + 0.11*blue + 0.59*green)
        
max_filter = np.ones((5,5))

i  = 0
u = 0

row = int(x[0]/5)
col = int(x[1]/5)

for x in range(row):
        for x in range(col):
            
            I_new = [[max_filter[0,0]*grayscale[0+u,0+i],max_filter[0,1]*grayscale[0+u,1+i],max_filter[0,2]*grayscale[0+u,2+i],max_filter[0,3]*grayscale[0+u,3+i],max_filter[0,4]*grayscale[0+u,4+i]],
                 [max_filter[1,0]*grayscale[1+u,0+i],max_filter[1,1]*grayscale[1+u,1+i],max_filter[1,2]*grayscale[1+u,2+i],max_filter[1,3]*grayscale[1+u,3+i],max_filter[1,4]*grayscale[1+u,4+i]],
                 [max_filter[2,0]*grayscale[2+u,0+i],max_filter[2,1]*grayscale[2+u,1+i],max_filter[2,2]*grayscale[2+u,2+i],max_filter[2,3]*grayscale[2+u,3+i],max_filter[2,4]*grayscale[2+u,4+i]],
                 [max_filter[3,0]*grayscale[3+u,0+i],max_filter[3,1]*grayscale[3+u,1+i],max_filter[3,2]*grayscale[3+u,2+i],max_filter[3,3]*grayscale[3+u,3+i],max_filter[3,4]*grayscale[3+u,4+i]],
                 [max_filter[4,0]*grayscale[4+u,0+i],max_filter[4,1]*grayscale[4+u,1+i],max_filter[4,2]*grayscale[4+u,2+i],max_filter[4,3]*grayscale[4+u,3+i],max_filter[4,4]*grayscale[4+u,4+i]]]
            
            
            slide_img = [[grayscale[0+u,0+i],grayscale[0+u,1+i],grayscale[0+u,2+i],grayscale[0+u,3+i],grayscale[0+u,4+i]],
                        [grayscale[1+u,0+i],grayscale[1+u,1+i],grayscale[1+u,2+i],grayscale[1+u,3+i],grayscale[1+u,4+i]],
                        [grayscale[2+u,0+i],grayscale[2+u,1+i],grayscale[2+u,2+i],grayscale[2+u,3+i],grayscale[2+u,4+i]],
                        [grayscale[3+u,0+i],grayscale[3+u,1+i],grayscale[3+u,2+i],grayscale[3+u,3+i],grayscale[3+u,4+i]],
                        [grayscale[4+u,0+i],grayscale[4+u,1+i],grayscale[4+u,2+i],grayscale[4+u,3+i],grayscale[4+u,4+i]]]
            x = np.argwhere(slide_img == (np.amax(I_new)))
            
           
            y = np.shape(x)
            new_array= []
            for z in range(y[0]):
               q = ( x[z])
               q[1] = q[1]+i
               q[0] = q[0]+u
               
               new_array.append(q)
            l = (len(new_array))
            
            for s in range(l):
                p = np.array(new_array[s])
                index_array.append(p)
            
                
                
            if i == 0:
                    i = (i+1)*5
            elif i != 0:
                   i = i+5
                
        if u == 0:
                u = (u+1)*5
        elif u != 0:
               u = u+5
        i = 0
 
for o in index_array:

    new_img[o[0],o[1]] = 255 
