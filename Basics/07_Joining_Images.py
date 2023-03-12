import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\test_01.jpg")
img2 = cv2.imread(r"C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\test_02.jpg")

print(img1.shape)
print(img2.shape)

"""
NOTE:
1) Joining or Stacking of Images can be done either vertically or horizontally
2) Stacking is done through Numpy not OpenCV
3) All the Images should be of same size and channels
4) Input should be given in a Tuple
5) This is helpful when we want to visualize many images in the same script
"""

img2_resized = cv2.resize(img2,(img1.shape[1],img1.shape[0]))

horStackImg = np.hstack((img1,img1,img2_resized))
verStackImg = np.vstack((img1,img2_resized))


cv2.imshow("Horizontally Stacked Image",horStackImg)
cv2.imshow("Vertically Stacked Image",verStackImg)

cv2.waitKey(0)