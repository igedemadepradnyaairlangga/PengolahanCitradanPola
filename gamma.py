import cv2
import numpy as np
from cv2 import waitKey

def gammaCorrection(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to their
    #adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
    for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

img = cv2.imread("banteng.jpg")
gammaImg = gammaCorrection(img, 2.2)
cv2.imshow('Original image', img)
cv2.imshow('Gamma corrected image', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows() 