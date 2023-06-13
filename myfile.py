# ref:https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
# ref: https://python-forum.io/thread-25926.html
# ref : https://pynative.com/python-list-files-in-a-directory/

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import glob
import os as os
import tkinter as tk
from tkinter import filedialog


# from tkinter import Tk for Python 3.x
#from tkinter.filedialog import askopenfilename
class myfile:
   def __init__(self):
      print("default constructor")

   def getfilelist(self,thefolder,extensionname: str):
    print("note: opencv filename can not using chinese~!!")
    allfiles = glob.glob(os.path.join(thefolder,extensionname))
    #print(len(allfiles));
    #print(allfiles);
    return allfiles



    #system pause
cv.waitKey(0)
