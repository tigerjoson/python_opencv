# ref:https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
# ref: https://python-forum.io/thread-25926.html
# ref : https://pynative.com/python-list-files-in-a-directory/
# ref :https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import glob
import os as os
import tkinter as tk
from tkinter import filedialog

# from tkinter import Tk for Python 3.x
#from tkinter.filedialog import askopenfilename


 # show an "Open" dialog box and return the path to the selected file
#thefolder = tk.filedialog.askdirectory();  



#def Binarization (convert image to black and white)
class myconverttogray():
    def __init__(self):
        self.path = 'default constructor'

    def methoda(self, path):
        self.path = path;
       # print(path);
        if cv.haveImageReader(thefile):
           ret, output1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV);
           plt.imshow(plt_image(output1));
           #cv.imshow('hi',output1)
           cv.imwrite(newfullpath, output1)
           #plt.savefig(newname)
           plt.close();
           #plt.show();
    #system pause
cv.waitKey(0)
 
