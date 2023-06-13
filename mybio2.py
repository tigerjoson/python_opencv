
from myconverttogray import *
from myfile import *

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import glob
import os as os
import tkinter as tk
from tkinter import filedialog




#A = myconverttogray();
#A.methoda(thefile,newfullpath)

thefolder = tk.filedialog.askdirectory();
print(thefolder)
ext = "*.jpg"
B = myfile();
print(ext)
mylist= B.getfilelist(thefolder,ext);
#print(mylist[1])
for f in mylist :

    image = cv.imread(f);
    basename = os.path.basename(f);
    path = f.replace(basename,'')
    print(f)
    newfullpath = path+"bio"+basename;
    A = myconverttogray();
    A.methoda(f,newfullpath)
