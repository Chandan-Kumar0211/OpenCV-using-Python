import cv2
import numpy as np

img = cv2.imread(r"C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\test_05.jpg")
print(img.shape)

kernel = np.ones((3,3),np.uint8)


# Resizing an Image
imgResize = cv2.resize(img,(840,620))


# Converting a coloured image to Gray Scale
imgGray = cv2.cvtColor(imgResize,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_window',imgGray)


# Blurring an Image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow('blur_window',imgBlur)


# Performing Canny Edge Detection
imgCanny = cv2.Canny(imgResize,200,250)
cv2.imshow('canny_window',imgCanny)


# Dilating an Image (As when we used canny edge detector, there were gaps in lines which should be continuous)
# This method helps to overccome that issue
imgDilate = cv2.dilate(imgCanny,kernel,iterations=2)
cv2.imshow('dilate_window',imgDilate)


# Eroding an Image
imgEroded = cv2.erode(imgDilate,kernel,iterations=2)
cv2.imshow('erode_window',imgEroded)


cv2.waitKey(0)




