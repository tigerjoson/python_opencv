#ref: https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
#https://chtseng.wordpress.com/2016/12/05/opencv-contour%E8%BC%AA%E5%BB%93/
import numpy as np
import cv2 as cv
path = r"C:\Users\tiger\Pictures\test\12250161_923817071027707_8371995491597490875_n.jpg"
img = cv.imread(path, cv.IMREAD_GRAYSCALE)

#hull = cv.convexHull(contours[,output[, Orientation_flag. [,boolean_coordinates_of_the_hull_point]]])

ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
for contour in contours:
 hull = cv.convexHull(contour)
 #print(type(hull))
 
 
