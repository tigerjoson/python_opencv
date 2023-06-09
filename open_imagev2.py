# ref :https://github.com/howarder3/ironman2020_OpenCV_photoshop/blob/master/Day02_%E5%9C%96%E7%89%87%E8%AE%80%E5%8F%96%E9%A1%AF%E7%A4%BA%E5%AD%98%E6%AA%94_image_load_show_save.ipynb
# ref : https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import glob

from IPython.display import clear_output

path = r""
 #print(cv.version)
#因opencv(BGR) 與  matplotlib(RGB)  顏色順序不同需轉換
def plt_image(imagebgr):
    image_rgb = cv.cvtColor(output1, cv.COLOR_BGR2RGB)
    return image_rgb;

#opencv can read
if cv.haveImageReader(path):
    print(cv.haveImageReader(path))
    image = cv.imread(path)
    
    ret, output1 = cv.threshold(image, 75, 255, cv.THRESH_BINARY);
    
    #cv.imshow('pic',output1)

    #pass to matplotlib.pyplot to draw
    plt.imshow(plt_image(output1))
    plt.show()
    #system pause
    cv.waitKey(0)
