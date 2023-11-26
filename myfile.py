import glob
# All files and directories ending with .txt and that don't begin with a dot:
print(glob.glob("C:\\Users\\tiger\\Pictures\\Saved Pictures\\*.txt")) 
# All files and directories ending with .txt with depth of 2 folders, ignoring names beginning with a dot:
print(glob.glob("C:\\Users\\tiger\\Pictures\\Saved Pictures\\*.jpg")) 

#or 
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
thefolder = tk.filedialog.askdirectory();
extensionname = "*.jpg"
#print(thefolder)
globstring = thefolder.join(extensionname)
print (globstring)
# note: opencv filename can not using chinese~!!
allfiles = glob.glob(os.path.join(thefolder,extensionname ))
print(allfiles);

