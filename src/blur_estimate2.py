# -*- coding: utf-8 -*-
import os

from numpy import *
from PIL import Image
from pylab import *
from scipy.ndimage import filters
from scipy.signal import argrelextrema

def locate_edge(arr, thresh=10.0):
    pass


cd = os.path.dirname(os.path.abspath(__file__))
fn = "test3.jpg"
fp = os.path.join(cd, fn)

# target row
r = 100

# raw image
imr = array(Image.open(fp).convert('L'))
imx0 = zeros(imr.shape)
filters.sobel(imr, 1, imx0)

figure()
gray()

subplot(121)
imshow(imx0)
subplot(122)
title(r'$\sigma=0$')
plot(range(len(imr[r])), imr[r])
plot(range(len(imx0[r])), imx0[r]) 

show()

a = argrelextrema(imx0[r], np.greater, order=4) 