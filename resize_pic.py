import cv2 as cv;
path =r'';
#the order must be right
#must call namedWindow
cvwindowname = "resize fig demo"
cv.namedWindow(cvwindowname,cv.WINDOW_KEEPRATIO);
#read picture return type = mat
imagemat = cv.imread(path);

cv.imshow(cvwindowname,imagemat);
windowtuple = cv.getWindowImageRect(cvwindowname);
xcoordinates = windowtuple[0];
ycoordinates = windowtuple[1];
width = windowtuple[2]
height = windowtuple[3]
#print(windowtuple)
#print(type(cv.getWindowImageRect(cvwindowname)))
cv.waitKey();
