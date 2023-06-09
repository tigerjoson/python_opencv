# ref:https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
# ref: https://python-forum.io/thread-25926.html

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import glob
from tkinter import Tk
# from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


 # show an "Open" dialog box and return the path to the selected file
filename = askopenfilename();

# note: filename can not using chinese~!!
cvpath = filename.replace("/","\\\\");
print(cvpath);
image = cv.imread(cvpath);
#cv.imshow('hi',image);


def plt_image(imagebgr):
    image_rgb = cv.cvtColor(output1, cv.COLOR_BGR2RGB)
    return image_rgb;

if cv.haveImageReader(cvpath):
    print(cv.haveImageReader(cvpath))
        
    ret, output1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV);
    plt.imshow(plt_image(output1));
    plt.show();
elif image is None:
    print("None")
    exit(0)
else:
    exit(0)

    #system pause
cv.waitKey(0)
