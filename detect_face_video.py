import cv2
import numpy as np
import time
from time import sleep
cap=cv2.VideoCapture(0)
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while 1 :
	ret,image=cap.read()
	image1=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces=face.detectMultiScale(image1, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,0),2)
	cv2.imshow('image1', image)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.DestroyAllWindows()
