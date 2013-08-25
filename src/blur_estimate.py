# -*- coding: utf-8 -*-
from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
import os

"""
cd = os.path.dirname(os.path.abspath(__file__))
fn = "800px-Monticello_2010-10-29.jpg"
fp = os.path.join(cd, "data", fn)

im = array(Image.open(fp).convert('L'))
"""

im = array(Image.open("C:/DEV/Area52/home/joker/dev/moojoos/test.jpg").convert("L"))

figure()
gray()
imx = zeros(im.shape)
filters.sobel(im, 1, imx)
imshow(imx)
plot(range(len(im[255])), im[255])
show()