# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:49:46 2021

@author: Sammy
"""

import cv2
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print (len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCor == 3: objectType = "Tri"
            elif objCor == 4: 
                aspRatio = w/float(h)
                if aspRatio>0.95 and aspRatio<1.05: objectType = "Square"
                else:objectType = "Rectangle"
            elif objCor>4: objectType = "Ellipse"
            else: objectType = "None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            
            cv2.putText(imgContour,objectType,(int(x+(w/2)-10),int(y+(h/2)-10)),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),2)

path = "resource/detect_blob.png"
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

imgBlank = np.zeros_like(imgGray)
im_h = cv2.hconcat([imgGray,imgBlur,imgCanny,imgBlank])
getContours(imgCanny)
im_v=cv2.vconcat([img,imgContour])

cv2.imshow("image",im_h)
cv2.imshow("original", im_v)
#cv2.imshow("gray", imgGray)
#cv2.imshow("blur", imgBlur)
cv2.waitKey(0)