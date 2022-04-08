import cv2
from cv2 import waitKey
from matplotlib import pyplot as plt
import numpy as np 
img = cv2.imread("banteng.jpg")

cv2.imshow('Gambar Asli', img)
waitKey(0) 
#mengubah ke greyscale menggunakan function pada OpenCV
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
brightness = 100 
h, w = img2.shape[:2]
#perulangan untuk melakukan proses pertambahan 
for i in np.arange(h):
    for j in np.arange(w):
        a = img2.item(i, j)
        b = a + brightness
        if b > 255: 
             b = 255
        elif b < 0:
            b =0
        else:
            b =b
        img2.itemset((i, j), b)
cv2.imshow("Gambar perbaikan",img2)
waitKey(0)