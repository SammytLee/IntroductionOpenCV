# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:37:38 2021

@author: Sammy
"""

import cv2

cap = cv2.VideoCapture("vtest.avi")

while True:
    success, img = cap.read()
    
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break