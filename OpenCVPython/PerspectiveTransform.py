# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:36:58 2021

@author: Sammy
"""

import cv2
import numpy as np

width,height = 250,350
img = cv2.imread("cards.png")
#location of middle row  1st column   
pts1 = np.float32([[119,183],[195,216],[65,293],[140,330]])
pts2 = np.float32([[0, 0], [width, 0],[0, height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height) )
cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)