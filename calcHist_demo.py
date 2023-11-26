# demo ref: https://docs.opencv.org/3.4/d8/dbc/tutorial_histogram_calculation.html
# https://blog.gtwang.org/programming/python-opencv-matplotlib-plot-histogram-tutorial/
#ref: https://docs.opencv.org/3.4/d1/db7/tutorial_py_histogram_begins.html
# ref : https://steam.oxxostudio.tw/category/python/example/matplotlib-subplot.html
#from __future__ import print_function
#from __future__ import division
import cv2 as cv
import numpy as np
import argparse
import matplotlib.pyplot as plt
print(type(plt))

parser = argparse.ArgumentParser(description='Code for Histogram Calculation tutorial.')
#parser.add_argument('--input', help='Path to input image.', default='lena.jpg')
#args = parser.parse_args()
#src = cv.imread(cv.samples.findFile(args.input))
path = r"C:\Users\tiger\Pictures\Saved Pictures\2021-12-11 11 47 24.jpg"
src = cv.imread(path);
if src is None:
    print('Could not open or find the image', args.input)
    exit(0)

#分離RGB三通道使用 
bgr_planes = cv.split(src)
print(bgr_planes)
histSize = 256
histRange = (0, 256) # the upper boundary is exclusive
accumulate = False
# cv.calcHist() to find the histogram of the full image. 
blue_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate);
grenn_hist = cv.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate);
red_hist = cv.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate);
#set histogram width
hist_w = 512;
#set histogram height
hist_h = 400;
bin_w = int(round(hist_w/histSize));

#Cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]	) ->	hist
#images	
    #Source arrays.
#    They all should have the same depth, CV_8U, CV_16U or CV_32F , 
#   and the same size. Each of them can have an arbitrary number of channels.
#nimages
#	Number of source images.
#channels	
#   List of the dims channels used to compute the histogram.
# The first array channels are numerated from 0 to images[0].channels()-1 , 
# the second array channels are counted from images[0].channels() to images[0].channels() + images[1].channels()-1, 
# and so on.

#mask
#	Optional mask. 
# If the matrix is not empty, it must be an 8-bit array of the same size as images[i] . 
# The non-zero mask elements mark the array elements counted in the histogram.

#hist
#	Output histogram, which is a dense or sparse dims -dimensional array.
#dims
#	Histogram dimensionality that must be positive and not greater than CV_MAX_DIMS
# (equal to 32 in the current OpenCV version).

#histSize
#	Array of histogram sizes in each dimension.

#histRange
#Array of the dims arrays of the histogram bin boundaries in each dimension.
# When the histogram is uniform ( uniform =true), 
# then for each dimension i it is enough to specify the lower (inclusive) boundary L0 of the 0-th histogram bin
# and the upper (exclusive) boundary UhistSize[i]−1 for the last histogram bin histSize[i]-1 . 
# That is, in case of a uniform histogram each of ranges[i] is an array of 2 elements.
# When the histogram is not uniform ( uniform=false ), then each of ranges[i] contains histSize[i]+1 elements: L0,
# U0=L1,U1=L2,...,UhistSize[i]−2=LhistSize[i]−1,UhistSize[i]−1 . 
# The array elements, that are not between L0 and UhistSize[i]−1 , are not counted in the histogram.

#uniform	
# Flag indicating whether the histogram is uniform or not (see above).

#accumulate
#	Accumulation flag. 
#If it is set, the histogram is not cleared in the beginning when it is allocated.
# This feature enables you to compute a single histogram from several sets of arrays, 
# or to update the histogram in time.

#np.zeros(5) => array([ 0.,  0.,  0.,  0.,  0.])
#np.zeros(a,b,c) => 3-d array
#np.zeros(7, dtype = int) => type = int
# np.uint8 => 8-bit unsigned integer (0 to 255).
 
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
cv.normalize(blue_hist, blue_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(grenn_hist, grenn_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(red_hist, red_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
#range(start, stop, step)
for i in range(1, histSize):
    #	cv.line(img, pt1, pt2,Line_color[, line_thickness[, lineType[, shift]]]	) ->img
    #pt1=>First point of the line segment.
    #pt2=>Second point of the line segment.

    cv.line(histImage,(bin_w*(i-1),hist_h-int(blue_hist[i-1])),(bin_w*(i),hist_h-int(blue_hist[i])),(255,0,0),thickness=2);
    cv.line(histImage,(bin_w*(i-1),hist_h-int(grenn_hist[i-1])), (bin_w*(i),hist_h-int(grenn_hist[i])),(0,255,0),thickness=2);
    cv.line(histImage,(bin_w*(i-1),hist_h-int(red_hist[i-1])),(bin_w*(i),hist_h-int(red_hist[i])),(0,0,255),thickness=2)
#cv.imshow('Source image', src)
#cv.imshow('calcHist Demo', histImage)
def plt_image(output1):
    image_rgb = cv.cvtColor(output1, cv.COLOR_BGR2RGB)
    return image_rgb;
if cv.haveImageReader(path):
    ret, output1 = cv.threshold(src, 127, 255, cv.THRESH_BINARY_INV);
    ret, output2 = cv.threshold(histImage, 127, 255, cv.THRESH_BINARY_INV);
    #plt.subplot (row, column, index)
    #= plt.subplot(2,3,1)
    #plt=>2*3之 arrays 
    plt.subplot(231);
    plt.imshow(plt_image(output1));
    plt.subplot(232);
    plt.imshow(plt_image(output2));
    plt.show()
   
