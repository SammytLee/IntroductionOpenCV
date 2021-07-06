# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:48:35 2021

@author: Sammy
"""

import cv2 
import numpy as np

img = cv2.imread("starry_night.jpg")
imgResize = cv2.resize(img,(300,400))
print(img.shape)
print(imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("Image", img)
cv2.imshow('Resize', imgResize)
cv2.imshow('Cropped', imgCropped)

cv2.waitKey(0)