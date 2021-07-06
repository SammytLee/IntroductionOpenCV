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

### ColorFinder
This project creates a mask to filter out certain values in HSV space. It first uses the webcam to capture images and sliders to filter out the HSV values you are looking for into a binary mask which then is passed through a mask that allows only that color to shine be captured. 

### CreatingAndImplementingTrackBarMask
This project is similar to the ColorFinder project. It uses an image instead of a webcam to capture certain parts of the image using Trackbars. The image used is starry night from the OPENCV samples.

### CreatingShapesAndText
This project creates different shapes using the built-in OPENCV functions and shows how you can implement text or captioning on a screen.

### DetectShapes
This program uses an algorithm to detect some basic shapes the input image. The image used is called detect_blob and it is from the OPENCV library. It uses an algorithm where it draws contours around an object in the image as long as the area of the image is greater than 500. It uses an approximation of a polygon and the corners found to detect the shape. If the corners = 3, it's a triangle. If the corners = 4, it's a square or rectangle; if the corners > 4, then it's an ellipse. 


## Project Status
complete

## Sources
These exercises were done following Muratza's Workshop on youtube.
The link provided is https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=19s is the source of the 
walkthrough.
