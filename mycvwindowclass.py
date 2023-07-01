#ref:https://stackoverflow.com/questions/28327020/opencv-detect-mouse-position-clicking-over-a-picture
#ref:https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga89e7806b0a616f6f1d502bd8c183ad3e
#ref :
import cv2 as cv;
import tkinter as tk;
from tkinter import filedialog;


#path = r"C:\Users\tiger\Pictures\Saved Pictures\2021-12-11 11 47 24.jpg"
#the order must be right
#must call namedWindow
class mycvwindowclass:
    def __init__(self):
        self._cvwindowname = "resize window";
        self._file = r"C:\Users\tiger\Pictures\test\12250161_923817071027707_8371995491597490875_n.jpg";
    def setwindowname(self, cvwindowname: str):
        self._cvwindowname = cvwindowname
   
    def getWindowname(self):
        return self._cvwindowname;
    def setf(self):
        self._file = tk.filedialog.askopenfilename();
    def setfile(self,path):
        self._file = path;
    def getfile(self):
        return self._file;
       
    def show (self):
        cvwindowname = self.getWindowname();
        cv.namedWindow(cvwindowname,cv.WINDOW_KEEPRATIO);
        path = self.getfile();
#read picture return type = mat
        imagemat = cv.imread(path);
        cv.imshow(cvwindowname,imagemat);
        windowtuple = cv.getWindowImageRect(cvwindowname);
        xcoordinates = windowtuple[0];
        ycoordinates = windowtuple[1];
        width = windowtuple[2]
        height = windowtuple[3]
        
        print(windowtuple)
#print(type(cv.getWindowImageRect(cvwindowname)))
        
       #cv.waitKey();