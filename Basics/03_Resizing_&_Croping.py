import cv2
import numpy as np

img = cv2.imread(r'C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\test_05.jpg')
print(img.shape)


# Resizing an Image
imgResize = cv2.resize(img,(430,540))
print(imgResize.shape)


# Cropping an Image
imgCropped = img[200:1000,100:700]
print(imgCropped.shape)


cv2.imshow('Original Image',img)
cv2.imshow('Resized Image',imgResize)
cv2.imshow('Cropped Image',imgCropped)


cv2.waitKey(0)