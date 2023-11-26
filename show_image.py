import cv2 as cv;
import tkinter as tk;
from tkinter import filedialog;

thefile = tk.filedialog.askopenfile();

imagemat = cv.imread(thefile.name);
cv.imshow("hi",imagemat);
#me = cv.setMouseCallback(myobj.getWindowname(),mycvevent.show_event);
def showbgr( event,  x,  y,  flags,userdata):
    if event == cv.EVENT_LBUTTONDOWN:
        print(imagemat[x,y]);
cv.setMouseCallback("hi",showbgr)
cv.waitKey();
