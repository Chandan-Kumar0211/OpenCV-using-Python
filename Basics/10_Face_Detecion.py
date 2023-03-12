"""
To Detect FACES, we are going to use the method proposed by VIOLA and JONES.
It's the earliest method that allows real time object detection.

To detect FACES, we collect lots of:
 1) Positives: Contains images of FACES
 2) Negatives: Contains images of anything but not FACES
Using these Positives and Negatives we train and create a cascade file that
will help us find FACES in new Images

# NOTE: Here, we will use a pretrained file provided by OpenCV
Although we can create our own custom cascade file and use it to detect FACES.
(We can create custom cascade to detect anything we need)

"""


import cv2

faceCascade = cv2.CascadeClassifier("..\Resources\haarcascades\haarcascade_frontalface_default.xml")

img = cv2.imread(r"C:\Users\CHAND\PycharmProjects\OpenCV_Murtazas_Workshop\Resources\test_01.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgDuplicate = img.copy()

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(imgDuplicate,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Original Image",img)
cv2.imshow("face detected Image",imgDuplicate)
cv2.waitKey(0)