import cv2
import numpy as np

# Reading Images

img = cv2.imread(r"C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\test_02.jpg")
cv2.imshow('img_window',img)
cv2.waitKey(2000)



# Reading Videos

cap = cv2.VideoCapture(r"C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\test_video.mp4")

# true = 0
# false = 0
#
# print(true)
# print(false)

while True:
    # Each frame is captured in 'img' variable and then 'success' variable will give result in boolen value that
    # each frame is successfully captured or not
    success, img = cap.read()
    cv2.imshow('vdo_window',img)

    # if success==True:
    #     true += 1
    # else:
    #     false += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# print(true)
# print(false)

# Reading WebCam

web_cap = cv2.VideoCapture(0)

while True:
    success, img = web_cap.read()
    cv2.imshow('webCam_window',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()




