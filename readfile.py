
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
ext = "*.txt"
mystring = "ulz76";
B = myfile();
print(ext)
mylist= B.getfilelist(thefolder,ext);
#print(mylist[1])
for f in mylist :
#    print(f)
    with open(f, encoding='UTF-8') as content:
     lines = content.readlines();
     for line in lines:
         if line.find(mystring):
            print(f)
            print(line)
            cv.waitKey(0);
         else :
            print("not found")

content.close();
print("fin")
