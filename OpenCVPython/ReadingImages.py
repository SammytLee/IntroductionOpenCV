# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:08:01 2021

@author: Sammy
"""

import cv2

print("Package Imported")

img = cv2.imread('lena.jpg', 1)

cv2.imshow("output",img)
cv2.waitKey(0)