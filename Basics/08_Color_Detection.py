import cv2
import numpy as np

def empty(a):
    pass

img = cv2.imread(r"C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\lambo.jpg")
imgResized = cv2.resize(img,(512,512))


"""
Creating a trackbar for getting the optimum min and max number for 
Hue, Saturation and Value which we will use to extract the exact required color
"""

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)

# # First we set up defaults values
# cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
# cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
# cv2.createTrackbar("Saturation Min","TrackBars",0,255,empty)
# cv2.createTrackbar("Saturation Max","TrackBars",255,255,empty)
# cv2.createTrackbar("Value Min","TrackBars",0,255,empty)
# cv2.createTrackbar("Value Max","TrackBars",255,255,empty)

# Here, we are putting our optimum values which we got after sliding the above default value trackbars
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",25,179,empty)
cv2.createTrackbar("Saturation Min","TrackBars",33,255,empty)
cv2.createTrackbar("Saturation Max","TrackBars",255,255,empty)
cv2.createTrackbar("Value Min","TrackBars",44,255,empty)
cv2.createTrackbar("Value Max","TrackBars",255,255,empty)

# Now reading these trackbar values so that we can apply this on our Images

while True:
    imgHSV = cv2.cvtColor(imgResized,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Min","TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Max","TrackBars")
    v_min = cv2.getTrackbarPos("Value Min","TrackBars")
    v_max = cv2.getTrackbarPos("Value Max","TrackBars")

    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    maskImg = cv2.inRange(imgHSV,lower,upper)
    resultImg = cv2.bitwise_and(imgResized,imgResized,mask=maskImg)

    # horStackImg_1 = np.hstack((imgResized,imgHSV))
    # horStackImg_2 = np.hstack((maskImg,resultImg[:,:,0]))
    #
    # verStackImg = np.vstack((horStackImg_1[:,:,0],horStackImg_2))

    cv2.imshow("Resized Image",imgResized)
    cv2.imshow("HSV Image",imgHSV)
    cv2.imshow("Masked Image", maskImg)
    cv2.imshow("Result Image",resultImg)
    # cv2.imshow("All Image Stacked Together",verStackImg)
    cv2.waitKey(1)


