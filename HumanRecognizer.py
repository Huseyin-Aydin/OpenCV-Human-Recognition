import cv2
videoPath="" #Insert your video path here
boxColor=(255,0,0)
cap=cv2.VideoCapture(videoPath)
mycascade=cv2.CascadeClassifier(".\\haarcascade_frontalface_default.xml")
font1=cv2.FONT_HERSHEY_SIMPLEX

while True:
	ret,frame=cap.read()
	frame=cv2.flip(frame,1)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	obj=mycascade.detectMultiScale(gray,1.3,7)
	for (x,y,w,h) in obj:
		cv2.rectangle(frame,(x,y),(x+w,y+h),boxColor,2)
		cv2.putText(frame,"Human",(x,y),font1,1,boxColor,cv2.LINE_4)

	cv2.imshow("Object",frame)

	if cv2.waitKey(1) & 0XFF==ord("q"):
		break

cap.release()
cv2.destroyAllWindows()
