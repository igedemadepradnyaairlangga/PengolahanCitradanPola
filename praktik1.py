import cv2
import numpy as np
# read the image
image = cv2.imread('banteng.jpg')
# apply the 3x3 mean filter on the image
kernel = np.ones((3,3),np.float32)/9
processed_image = cv2.filter2D(image,-1,kernel)
mean_blur = cv2.blur(image,(5,5))
gaussian_blur = cv2.GaussianBlur(image,(5,5),0)
# display image
cv2.imshow('Gambar Asli Banteng', image)
cv2.imshow('Mean Filter Processing', processed_image)
cv2.imshow('Mean Blur', mean_blur)
cv2.imshow('Gaussian Blur', gaussian_blur)
# pause the execution of the script until a key on the keyboard is pressed
cv2.waitKey(0)