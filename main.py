#Tanay Karve
#Driving using gesture recognition and augmented steering wheel
#V1.4

import cv2
import numpy as np
import math
import pyvjoy
from controls import xAxis, yAxis,Brake,j,reCentre

cap = cv2.VideoCapture(0)
Dir="-->"

while(1):
	
	_,img=cap.read()
	im=img
	img=img[150:450,80:500] #Define RegionOfInterest
	im=cv2.rectangle(im,(500,150),(80,450),(0,255,0),2)
	
	lower=np.array([0,20,150]) #HSV ranges for skin color
	upper=np.array([20,255,255])
	
	converted=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #convert BGR image to HSV image
	skinMask=cv2.inRange(converted,lower,upper) 
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
	skinMask=cv2.morphologyEx(skinMask,cv2.MORPH_CLOSE,kernel)
	skinMask = cv2.dilate(skinMask, kernel, iterations = 4)
	skinMask = cv2.GaussianBlur(skinMask, (7,7), 0)
	skin=cv2.bitwise_and(img,img,mask=skinMask)
	im2,contours,hierarchy=cv2.findContours(skinMask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#fit contours to hand regions
	
	try:

		cnt=max(contours,key=lambda x:cv2.contourArea(x))
		for ind,ct in enumerate(contours):#Iterate over all contours in frame
			M=cv2.moments(contours[ind])
			area=int(M["m00"])
			if area in range(6000,13000):#Ignore other contours that are not of hands 
				m1=cv2.moments(contours[0])
				m2=cv2.moments(contours[1])
				x1=int(m1["m10"]/m1["m00"])
				y1=int(m1["m01"]/m1["m00"])
				x2=int(m2["m10"]/m2["m00"])
				y2=int(m2["m01"]/m2["m00"])
				slope=math.tan(((y2-y1)/(x2-x1)))*100#convert the slope into %
				slope=round(slope,2)
			
				if slope>0:
					Dir="<--"
				else:
					Dir="-->"
								
				distance=math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
				distance=round((distance/300)*100,2)#convert distance from 0 - 300 into %
			
				if(distance>100):#limit distance to 100
					distance=100
				if slope>100:#limit angle to 100
					slope=100
				elif slope< -100:
					slope=-100
			
				cv2.line(im,(x1,y1),(x2,y2),(100,255,0),5)#plot line between centres of two hands
				cv2.putText(im,"Turning:"+Dir+str(slope)+"deg",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
				cv2.putText(im,"Acceleration:"+(str(distance)),(50,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
				xAxis(slope)#set xAxis on Joystick to the slope %
				yAxis(distance)#set yAxis on Joystick to speed %
				
			else:
				if area>13000 and len(contours)==1:#If area is of two hands joined
					cv2.putText(im,"BRAKE",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)
					Brake()
				
	except ValueError:#If hands are out of the frame
		reCentre()

	except:
		pass

	cv2.imshow('main cam',im)
	cv2.imshow('segment',skin)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.waitKey(0)
cv2.destroyAllWindows()
