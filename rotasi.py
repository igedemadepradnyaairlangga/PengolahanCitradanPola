import cv2
from cv2 import waitKey
import numpy as np

img = cv2.imread("lena.jpg")
cv2.imshow('Gambar Asli', img)
H, W = img.shape[:2]

M = np.float32([[1,0,100],[0,1,50]])
hasil = cv2.warpAffine(img,M,(W,H))
cv2.imshow('Gambar Asli', img)
cv2.imshow('Hasil Translasi', hasil)
cv2.waitKey(0)
waitKey(0)
