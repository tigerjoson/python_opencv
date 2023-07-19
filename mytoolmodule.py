#ref:https://stackoverflow.com/questions/28327020/opencv-detect-mouse-position-clicking-over-a-picture
#ref:https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga89e7806b0a616f6f1d502bd8c183ad3e
#ref :
import cv2 as cv;
import tkinter as tk;
from tkinter import filedialog;
import glob
import os
import pathlib
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
class myfileclass():
    def __init__(self):
        self._path = r"C:\\Users\\tiger\\Pictures\\test\\"  
        self._extensionname=r"*jpg"
        #print("default constuct=",glob.glob(self._path+self._extensionname))
    def get_path(self):
        return self._path
    def set_path(self, foldername: str):
        self._path=foldername
    def set_p(self):
        print("tk.filedialog.askdirectory();");
        thefolder = tk.filedialog.askdirectory();
        self._path = thefolder
        print("self.get_path()=",self.get_path())
    
    def set_ext(self, extensionname: str):
        self._extensionname = extensionname;
                
    def get_ext(self):
        return self._extensionname
    def get_list(self):
        searchstring = os.path.join(thefolder,extensionname);
        print("searchstring=",searchstring)
        allfiles = glob.glob(searchstring)
        #print(allfiles);
        
    def getfilelist(self): 
        thefolder = self.get_path();
        #print ("thefolder=",thefolder)
        extensionname = self.get_ext();
        #print ("extensionname=",extensionname)
        globresults= glob.glob(thefolder+"\\"+extensionname);
       # print(type (globresults))
       
        return globresults
    
    def rename (self,fullfilename_src,newfilename:str):
        filename = newfilename+os.path.splitext(os.path.basename(fullfilename_src))[0]
        ext = pathlib.Path(fullfilename_src).suffix
       # print(ext)
        self._path = os.path.dirname(fullfilename_src)
        #print(self.get_path()) ;
        fullfilenewname = self.get_path()+"//"+filename+ext
        print(fullfilenewname)
        
        #n = newfilename.join(filename)
        #print(n)
