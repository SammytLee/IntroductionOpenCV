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

### DocumentScanner
This project uses a webcam to a piece of paper or a note at an angle and warps it such that it looks as if the image is directly under the camera and takes a picture of it. Similar to a document scanner.
#### preProcessing
this function changes the colored image to gray scaled and creates a threshold for just the document selected through Canny Edge Detection
#### getContours
this function creates a contour around the object scanned. It looks for the biggest area. 
#### reorder
This function simply reorders the points such that we can transform the images perspective
#### getWarp
This function warps the image such that its perspective seems to be dead on. The image is then slightly cropped to only show the scanned part.

### FaceDetection
This project uses a Cascade Classifier for face detection. It simply draws a box around what is believed to be a face. The image used is lena from the OPENCV library.

### ImageCroppingAndResizing
This program crops and resizes images through built-in functions in OPENCV. The image used is starry-night from the OPENCV library. It shows a resized and cropped image as its outputs.

### NumberPlateDetection
This project uses a Cascade Classifier for number plate detection. A box is then drawn to around the number plate to show what it is detecting

### Perspective Transform
This project uses cards in different orientations to show how to do a perspective transform such that we can change an off center image to be centered. 

### Project1
This seems to be a copy of ColorDetectionAndDraw.

### ReadingImages
This project just reads an image and shows the read image.

### ReadingVideo
This project reads and shows a video in OPENCV.

### ReadingWebcam
This project show how to capture and show a webcam in OPENCV

### StackingImages
This project shows how to stack images in OPENCV through vstack or hstack.
## Project Status
complete

## Sources
These exercises were done following Muratza's Workshop on youtube.
The link provided is https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=19s is the source of the 
walkthrough.
