import cv2
import numpy as np
first_frame=None

video=cv2.VideoCapture(0)

while True:

    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(29,29),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)
    (contour,hierarchy)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contours in contour:
        if cv2.contourArea(contours) < 1000:
            continue
        (x,y,w,h)=cv2.boundingRect(contours)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("gray", gray)
    cv2.imshow("delta",delta_frame)
    cv2.imshow("threshold",thresh_frame)
    cv2.imshow("color",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()