# importing required libraries of opencv 
import cv2 
import numpy as np 
# importing library for plotting 
from matplotlib import pyplot as plt 
# reads an input image 
img = cv2.imread('banteng.jpg') 
c = 75 / np.log(1 + np.max(img)) 
log_img = c*(np.log(img + 1)) 
# Specify the data type so that 
# float value will be converted to int 
log_img = np.array(log_img, dtype = np.uint8) 
# find frequency of pixels in range 0-255 
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
cv2.imshow('Gambar asli', img) 
# show the plotting graph of an image 
plt.imshow(img) 
plt.imshow(log_img) 
plt.show() 