import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# fetch image
img = cv.imread('banteng.jpg', cv.COLOR_BGR2GRAY) 
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Prewitt operator
kernelx = np.array([[1,1,1], [0,0,0], [-1,-1,-1]], dtype=int)
kernely = np.array([[-1,0,1], [-1,0,1], [-1,0,1]],dtype=int)

x = cv.filter2D(img, cv.CV_16S, kernelx)
y = cv.filter2D(img, cv.CV_16S, kernely)

# turn to uint8, image fusion
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y) 
Prewitt = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# Display graphics
titles = ['Original image', 'Prewitt operator']
images = [rgb_img, Prewitt]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show() 