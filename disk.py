#https://ckyrkou.medium.com/color-thresholding-in-opencv-91049607b06d
#black:	rgb(0, 0, 0)
#https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html
from mytoolmodule import *
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import glob
import os as os
import tkinter as tk
from tkinter import filedialog

#A = myconverttogray();
#A.methoda(thefile,newfullpath)


ext = "*.jpg"
B = myfileclass();
B.set_p();
B.set_ext(ext)
filelist = B.getfilelist();
for f in filelist:
    targert = B.get_new_fullname(f,"bio")
    #print(f)
    if cv.haveImageReader(f):
        #print(cv.haveImageReader(thefullfilename))
        image = cv.imread(f);
        ret, output1 = cv.threshold(image, 75, 255, cv.THRESH_BINARY);
        cv.imwrite(targert,output1)
    elif image is None:
        print("None")
        exit(0)
    else:
        exit(0)

    #system pause
    cv.waitKey(0)
