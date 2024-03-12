# Import Libraries
import cv2
import numpy as np

# Calling the image and converting in binary
frame  = cv2.imread("C:/Users/nisar/Desktop/Projects/ENPM 673 Midterm/Q1image.png")
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ret, frame = cv2.threshold(frame, 127, 255, 0)

kernel = np.ones((23,23),np.uint8) # Creating a kernel for erosion operation
erode = cv2.erode(frame, kernel)   # Perfoming erosion on the image to seperate the coins
cnt,hir = cv2.findContours(erode, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE) # Finding the contours in the image
x = (len(cnt)) # Counting the contours to get the number of coins

print(f"The number of coins in the image are {x}")
cv2.imshow("base_ image", frame)
cv2.imshow("erode_image", erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
