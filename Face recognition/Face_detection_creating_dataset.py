# Creating Dataset by Adding Numbers of data
import cv2
import matplotlib.pyplot as plt
import numpy as np
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
face_cascade1 = cv2.CascadeClassifier('cascades/data/haarcascade_profileface.xml')
cap = cv2.VideoCapture(0)
ID = input('Enter User ID \n')
sample_num = 0
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
    faces1 = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        sample_num = sample_num+1
        cv2.imwrite("dataSet/User."+ID+'.'+ str(sample_num) + ".jpg", gray[y:y+h,x:x+w])
    for (x,y,w,h) in faces1:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        sample_num = sample_num+1
        cv2.imwrite("dataSet/User."+ID+'.'+ str(sample_num) + ".jpg", gray[y:y+h,x:x+w])

    cv2.imshow('frame',frame)
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break
    elif sample_num>100:
        break

cap.release()

cv2.destroyAllWindows()