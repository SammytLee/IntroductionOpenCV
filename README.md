# IntroductionOpenCV
Basic OpenCV projects used to get familiar with the OPENCV library

## Introduction
Theses are simple projects done in OpenCV. They are used to simply introduce different functions available in the library.

## Technologies
* Python 3.6  
* OpenCV 4.5.1

## Launch
A webcam may be necessary for some of the projects. Videos and images included come from samples in the OPENCV repository. 

## Features
### BasicFunctions
 This project uses the lena.jpg image to show the differences between some of the image processing filters available to OPENCV these include:
 * BGR to GRAY
 * Gaussian Blur
 * Canny Edge Detection
 * Dilation
 * Erosion

### ColorDetectionAndDrawing
The main objective of this project is to detect a color of an object through creating a mask. And then using the object to draw on a screen captured by the webcam
#### findColor
This function creates a binary mask around the color that in myColor.
##### parameters
* img is the captured screen
* myColor is the color of the object in BGR
* myColorValues are the colors that you want portrayed on the screen.
#### getContours
This function creates a box around the object and returns points for the center top of the object.
#### drawOnCanvas
This function creates a circle at the center top point of the bounding box and draws it on the screen. 

## Project Status
complete

## Sources
These exercises were done following Muratza's Workshop on youtube.
The link provided is https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=19s is the source of the 
walkthrough.
