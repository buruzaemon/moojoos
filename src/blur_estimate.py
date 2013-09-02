# -*- coding: utf-8 -*-
from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
import os

cd = os.path.dirname(os.path.abspath(__file__))
fn = "test.jpg"
fp = os.path.join(cd, fn)

# target row
r = 1000

# raw image
imr = array(Image.open(fp).convert('L'))

# apply gaussian filter to reduce noise
img2 = filters.gaussian_filter(imr, 2)
img3 = filters.gaussian_filter(imr, 3)
img4 = filters.gaussian_filter(imr, 4)

figure()
gray()

imx2 = zeros(imr.shape)
filters.sobel(img2, 1, imx2)
subplot(231)
imshow(imx2) 
subplot(234)
title(r'$\sigma=2$')
plot(range(len(img2[r])), img2[r])
plot(range(len(imx2[r])), imx2[r]) 

imx3 = zeros(imr.shape)
filters.sobel(img3, 1, imx3)
subplot(232)
imshow(imx3)
subplot(235)
title(r'$\sigma=3$')
plot(range(len(img3[r])), img3[r])
plot(range(len(imx3[r])), imx3[r])

imx4 = zeros(imr.shape)
filters.sobel(img4, 1, imx4)
subplot(233)
imshow(imx4)
subplot(236)
title(r'$\sigma=4$')
plot(range(len(img4[r])), img4[r])
plot(range(len(imx4[r])), imx4[r])

show()