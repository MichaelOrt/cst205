import numpy as np
import cv2
from pprint import pprint

casc_class = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(casc_class)

eye_casc = 'haarcascade_eye.xml'
eye_cascade = cv2.CascadeClassifier(eye_casc)

if face_cascade.empty():
    print('WARNING: Cascade did not load')

my_video = cv2.VideoCapture(0)

while True:
    ret, frame = my_video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)


    cv2.imshow("face and eyes", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

my_video.release()
cv2.destroyAllWindows()