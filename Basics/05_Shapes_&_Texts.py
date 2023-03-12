import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)

cv2.imshow('Original Image',img)

img[:] = 215,80,154

"""
The above line is same as writing:
img[:,:] = 125,244,3   Or    img[:,:,0] = 125
                             img[:,:,1] = 244
                             img[:,:,2] = 30
"""

cv2.imshow('Modified Image',img)

# Drawing a Line on Image
cv2.line(img,(20,330),(444,222),(0,0,0),3)

# Drawing a diagonal line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,0),5)

# Drawing a Rectangle
cv2.rectangle(img,(32,44),(67,78),(0,0,125),2) # without filling area

cv2.rectangle(img,(132,144),(167,178),(0,0,125),cv2.FILLED) # with filled area


# Drawing a Circle
cv2.circle(img,(320,380),50,(255,255,0),5)


# Writing Texts on Image
cv2.putText(img,"Text on Image",(42,425),cv2.FONT_HERSHEY_COMPLEX,1,(32,132,32),2)


cv2.imshow("Various Shapes",img)
cv2.waitKey(0)