# Q) Take the grayscale image and create and initialize another image as all zeros. For each 5 x 5 window in the grayscale image, find out the maximum value and set the pixels with the maximum value in the 5x5 window as 255 in the new image.
# A) We convert the image in the grayscale and then make a kernel of the 5 by 5 matrix of ones. We multiply the kernel with the image and we do first column multiplications and then go down row by row. We also store the locations of the value with the max value. For all those values we change the 0 values to 255 in the new image that we create of zeros of the same size of the original image.

# Output
![10_nonmax](https://github.com/nisarg15/Basic_Computer_Vision/assets/89348092/35d2550d-58cd-439d-9c9d-1b5226362503)
