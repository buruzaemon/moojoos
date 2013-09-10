# -*- coding: utf-8 -*-
import os

from numpy import *
from PIL import Image
from pylab import *
from scipy.ndimage import filters
from peakdetect import *

cd = os.path.dirname(os.path.abspath(__file__))
fn = "test3.jpg"
fp = os.path.join(cd, fn)

# target row
r = 100

# raw image
imr = array(Image.open(fp).convert('L'))
imx0 = zeros(imr.shape)
filters.sobel(imr, 1, imx0)

a, b = peakdetect(imx0[r], lookahead=1)
a = zip(*a)
b = zip(*b)
maxx, maxy = a[0], a[1]
minx, miny = b[0], b[1]

figure()
gray()

subplot(121)
imshow(imx0)
subplot(122)
title(r'$\sigma=0$')
plot(range(len(imr[r])), imr[r])
plot(range(len(imx0[r])), imx0[r]) 
plot(maxx, maxy, "r+")
plot(minx, miny, "ro")

show()