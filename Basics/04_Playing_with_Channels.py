import cv2
import numpy as np

img = cv2.imread(r'C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\test_01.jpg')
print(img.shape)
print(type(img.shape))



cv2.imshow('Original Image',img)

# Visualizing each channel in Grayscale (single channel)
cv2.imshow('Grayscale Blue',img[:,:,0])
cv2.imshow('Grayscale Green',img[:,:,1])
cv2.imshow('Grayscale Red',img[:,:,2])


# Visualizing each channel in Color
(B,G,R) = cv2.split(img)

# NOTE: If we want to view effect of any one channel on the image,
#       we need to set the value of pixels of other two channels as zero
zeros = np.zeros(img.shape[:2],dtype="uint8")
print(zeros.shape)

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))     # Method 1
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))


"""
NOTE: 
In above two visualization method, in 1st method we are showing only one channel and that is why it is grayscale (here
intensity varies based on the channel specified) whereas in 2nd method, we are visualizing a combined 3 channels where
we keep the value of the one channel as it is and set the values of other two channels as zero. 
"""



cv2.waitKey(0)