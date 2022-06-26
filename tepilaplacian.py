import cv2 as cv
import matplotlib.pyplot as plt

# fetch image
img = cv.imread('banteng.jpg', cv.COLOR_BGR2GRAY) 
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Grayscale image processing
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplacian
dst = cv.Laplacian(grayImage, cv.CV_16S, ksize = 3)
Laplacian = cv.convertScaleAbs(dst)

# Display graphics
titles = ['Original image', 'the Laplacian operator']
images = [rgb_img, Laplacian] 
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show() 