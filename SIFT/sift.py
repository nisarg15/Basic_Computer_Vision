# Import the libraries
import numpy as np
import cv2

# Calling the images and converting them into grayscale
image1 = cv2.imread("C:/Users/nisar/Desktop/Projects/ENPM 673 Midterm/Q2imageB.png")
image2 = cv2.imread("C:/Users/nisar/Desktop/Projects/ENPM 673 Midterm/Q2imageA.png") 
image21 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image22 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Applying the feature detection algoritm 
sift = cv2.SIFT_create()
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

kp1, descriptors_1 = sift.detectAndCompute(image21,None)
kp2, descriptors_2 = sift.detectAndCompute(image22,None)

# Find the matches between 2 images and showing those matches on a seperate image
matches = bf.match(descriptors_1,descriptors_2)
matches = sorted(matches, key = lambda x:x.distance)
image3 = cv2.drawMatches(image1,kp1, image2, kp2, matches[:600], None)


points1 = np.zeros((len(matches), 2), dtype=np.float32)  
points2 = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
   points1[i, :] = kp1[match.queryIdx].pt    
   points2[i, :] = kp2[match.trainIdx].pt    

# Use homography
h, mask = cv2.findHomography(points1, points2, cv2.RANSAC,0.5)
 
height, width, channels = image2.shape

# Wrapping the image 2 over the image 1 over the same coordinate system using homography so that we can get stiched image
dst = cv2.warpPerspective(image1,h,(image2.shape[1] + image1.shape[1], image2.shape[0]))
dst[0:image2.shape[0],0:image2.shape[1]] = image2

# Cropping the unwanted black part from the image formed during stiching
def crop(frame):
    #crop top
    if not np.sum(frame[0]):
        return crop(frame[1:])

    if not np.sum(frame[-1]):
        return crop(frame[:-2])

    if not np.sum(frame[:,0]):
        return crop(frame[:,1:])

    if not np.sum(frame[:,-1]):
        return crop(frame[:,:-2])
    return frame

# Displaying the results
cv2.imshow("stitched_image.jpg", dst)
cv2.imshow("crop_stitched_image.jpg", crop(dst))
cv2.imshow("Matches_image", image3)
cv2.waitKey(0)
cv2.destroyAllWindows()
