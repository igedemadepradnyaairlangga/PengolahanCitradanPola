import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('banteng.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar asli",img)
cv2.imshow("Grayscale",gray)
cv2.waitKey(0)