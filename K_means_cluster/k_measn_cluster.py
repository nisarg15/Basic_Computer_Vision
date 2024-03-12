# Importing the libraries
import numpy as np
import cv2

# Random four intensity values of a grayscale image
a = 10
b = 100 
c = 180
d = 200

# defining the variables
A = []
B = []
C = []
D = []
val = []

# Calling the image and converting it into the grayscale image
img1 = cv2.imread("C:/Users/nisar/Desktop/Projects/ENPM 673 Midterm/Q4image.png") # trainImage
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
x = (np.shape(img1)) # Storing the shape of the image in a tuple

# K-Means 
for t in range(0,12): # Numbers of itrations
 for j in img1:
    for i in j:

# Finding the difference between the intensity of the image pixel and the random value
     w =  i-a
     x =  i-b
     y  = i-c
     z =  i-d
     
# Finding which values of the intensity is in which of the 4 clusters based of the diffrenece of intensities
     values = [w,x,y,z]
     values = np.absolute(values)
     low = np.argmin(values)
     if low == 0:
      A.append(i)
     elif low == 1:
      B.append(i)
     elif low == 2:
      C.append(i)
     else:
      D.append(i)

# Updating the mean value based of the clusters
 a = np.mean(A)
 b = np.mean(B)
 c = np.mean(C)
 d = np.mean(D)
 final_mean  = [a,b,c,d]

a = int(final_mean[0])
b = int(final_mean[1])
c = int(final_mean[2])
d = int(final_mean[3])

# Replacing each value of the pixel with the mean value based on which cluster it belongs    
for j in img1:
    for i in j:
        if i in range(np.min(A),np.max(A)):
            i = a
        elif i in range(np.min(B),np.max(B)):
            i = b
        elif i in range(np.min(C),np.max(C)):
            i = c
        else:
            i = d
        val.append(i) # Creating a 1-D list of the updated intensities

# Getting the image back from the 1-D list by resizing it accoring to the size of the orginal image
image = np.resize(val,(x[0],x[1]))

#Displaying the results
cv2.imshow("image", img1)
cv2.imshow("k_means_image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
