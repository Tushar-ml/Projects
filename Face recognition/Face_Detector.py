import cv2
import matplotlib.pyplot as plt
import numpy as np

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')
cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read('C:/Users/Tushar Goel/train.yml')
ids = 0
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    smile = smile_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        ids, conf = rec.predict(gray[y:y + h, x:x + w])
        if conf >= 30 and conf <= 100:
            if ids == 1:
                cv2.putText(frame, 'Tushar ' + str(conf), (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            elif ids == 2:
                cv2.putText(frame, 'Gaurav ' + str(conf), (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            elif ids == 3:
                cv2.putText(frame, 'Aayush ' + str(conf), (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            elif ids == 4:
                cv2.putText(frame, 'Chanchal ' + str(conf), (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            elif ids == 5:
                cv2.putText(frame, 'Neeraj ' + str(conf), (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, 'Unknown ', (x, y), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
    for (ex, ey, ew, eh) in eyes:
        frame = cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow('frame', frame)
    # for (sx,sy,sw,sh) in smile:
        #frame = cv2.rectangle(frame,(sx,sy),(sx+sw,sy+sh),(255,0,0),2)
        #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # elif sample_num>30:
    # break

cap.release()

cv2.destroyAllWindows()
