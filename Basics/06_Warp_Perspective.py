import cv2
import numpy as np

img = cv2.imread(r"C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\Unwarp_image.jpg")
print(img.shape)


# Performing Warp perspective to get its bird eye view

pts1 = np.int32([[75,375],[310,350],[95,699],[350,650]])
# print(pts1)
for x in range(4):
    cv2.circle(img,(pts1[x][0],pts1[x][1]),5,(200,15,200),cv2.FILLED)

width = 150
height = 200
pts2 = np.int32([[0,0],[width,0],[0,height],[width,height]])

pts1 = pts1.astype('float32')
pts2 = pts2.astype('float32')

matrix = cv2.getPerspectiveTransform(pts1,pts2) # IMPORTANT: Here, pts should be in float32 type

imgOut = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Unwarped Image",img)
cv2.imshow("Bird Eye View",imgOut)

cv2.waitKey(0)