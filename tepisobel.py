import cv2 as cv
import matplotlib.pyplot as plt

# fetch image
img = cv.imread('banteng.jpg', cv.COLOR_BGR2GRAY)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
 
# Grayscale image processing
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Sobel operator
x = cv.Sobel(grayImage, cv.CV_16S, 1, 0)
y = cv.Sobel(grayImage, cv.CV_16S, 0, 1)

# turn to uint8, image fusion
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Sobel = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# Display graphics
titles = ['Original image', 'Sobel operator']
images = [rgb_img, Sobel]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show() 