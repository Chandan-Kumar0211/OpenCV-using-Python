import cv2
import numpy as np
from stacking_images import stackImages


def getContours(img):

    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)

        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 3)
            perimeter = cv2.arcLength(cnt,True)
            # print(perimeter)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(len(approx))
            objCorner = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),2)

            if objCorner == 3:
                objType = "tri"
            elif objCorner == 4:
                aspectRatio = w/float(h)
                if aspectRatio >0.95 and aspectRatio <1.05:
                    objType = "Square"
                else:
                    objType = "Rect"
            elif objCorner > 4:
                objType = "Circle"
            else:
                objType = None

            cv2.putText(imgContour, objType,(x+(w//2)-20,y+(h//2)+5),
                        cv2.FONT_HERSHEY_COMPLEX,0.5, (0, 0, 0),2)





img = cv2.imread(r"C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\shapes.png")
# print(img.shape)


###########################---Image Pre-Processing---#######################################

imgResized = cv2.resize(img,(400,400))
imgGray = cv2.cvtColor(imgResized,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,3),0)
imgEdges_1 = cv2.Canny(imgGray,100,100)
imgEdges_2 = cv2.Canny(imgBlur,100,100)

imgBlank = np.zeros_like(imgResized)
imgContour = imgResized.copy()
###############################################################################################



getContours(imgEdges_2)

imgStacked = stackImages(0.8,([imgResized,imgGray,imgBlur],[imgEdges_1,imgEdges_2,imgContour]))
# cv2.imshow("Original Image",img)
# cv2.imshow("Resized Image",imgResized)
# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Edges on Gray Image",imgEdges_1)
# cv2.imshow("Edges on Blur Image",imgEdges_2)
cv2.imshow("Contour and Labelled Image",imgContour)
cv2.imshow("Stacked Images",imgStacked)
cv2.waitKey(0)