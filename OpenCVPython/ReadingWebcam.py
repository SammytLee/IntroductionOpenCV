# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:42:32 2021

@author: Sammy
"""

import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break