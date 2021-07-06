# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:01:32 2021

@author: Sammy
"""

import cv2
import numpy as np
img = cv2.imread('lena.jpg')

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow('Horizontal',imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)