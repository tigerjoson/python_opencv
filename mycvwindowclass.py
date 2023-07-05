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
        self._file = r"path";
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
    def getmat(self):
        path = self.getfile();
        #read picture return type = mat
        self._imagemat = cv.imread(path);
        return  self._imagemat
    def print_pointbgr(self,x,y):
        #numpy n-dimention arr
        ndarr = self.getmat();
        print(ndarr[x,y]);
    def show (self):
        cvwindowname = self.getWindowname();
        cv.namedWindow(cvwindowname,cv.WINDOW_KEEPRATIO);
        cv.imshow(cvwindowname,self.getmat());
        windowtuple = cv.getWindowImageRect(cvwindowname);
        xcoordinates = windowtuple[0];
        ycoordinates = windowtuple[ 1];
        width = windowtuple[2]
        height = windowtuple[3]
    
       #cv.waitKey();
