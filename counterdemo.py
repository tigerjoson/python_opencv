#https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

import numpy as np
import cv2 as cv
path = r"C:\Users\tiger\Pictures\test\12250161_923817071027707_8371995491597490875_n.jpg"
img = cv.imread(path, cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

#cv.threshold(src, thresh, maxval,thresholding type[, dst])
#Applies a fixed-level threshold to each array element.
# type =>multiple-channel array = ndarray
ret,thresh = cv.threshold(img,127,255,0)
#print("thresh type=",type(thresh))
#print("thresh=",thresh)
#cv.findContours(image, Contour retrieval mode, Contour approximation method[, contours[, hierarchy[, offset]]]) \
#The function retrieves contours from the binary image using the algorithm
#In Python, hierarchy is nested inside a top level array. 
#Use hierarchy[0][i] to access hierarchical elements of i-th contour.

contours,hierarchy = cv.findContours(thresh, 1, 2)
#print( cv.findContours(thresh, 1, 2))

cnt = contours[0]
#cv.moments(array[, binaryImage]) ->return moments.
M = cv.moments(cnt)
#print( M )

#Centroid x
cx = int(M['m10']/M['m00'])
#Centroid y
cy = int(M['m01']/M['m00'])
#cv.contourArea => float
area = cv.contourArea(cnt);
print(type(area));

arcLength = cv.arcLength(cnt,True);

############ Douglas-Peucker algorithm.
##epsilon = 0.1*cv.arcLength(cnt,True)
##approx = cv.approxPolyDP(cnt,epsilon,True)

############  Convex Hull algorithm.

cv.waitKey()