# -*- coding: utf-8 -*-
import os

from numpy import *
from PIL import Image
from pylab import *
from scipy.ndimage import filters


cd = os.path.dirname(os.path.abspath(__file__))
fn = "test3.jpg"
fp = os.path.join(cd, fn)

# target row
r = 100

# raw image
imr = array(Image.open(fp).convert('L'))

# apply gaussian filter to reduce noise
img2 = filters.gaussian_filter(imr, 2)
img3 = filters.gaussian_filter(imr, 3)
img4 = filters.gaussian_filter(imr, 4)

figure()
gray()

imx0 = zeros(imr.shape)
filters.sobel(imr, 1, imx0)

imx2 = zeros(imr.shape)
filters.sobel(img2, 1, imx2)

imx3 = zeros(imr.shape)
filters.sobel(img3, 1, imx3)

imx4 = zeros(imr.shape)
filters.sobel(img4, 1, imx4)

subplot(241)
imshow(imx0)
subplot(245)
title(r'$\sigma=0$')
plot(range(len(imr[r])), imr[r])
plot(range(len(imx0[r])), imx0[r]) 

subplot(242)
imshow(imx2) 
subplot(246)
title(r'$\sigma=2$')
plot(range(len(img2[r])), img2[r])
plot(range(len(imx2[r])), imx2[r]) 

subplot(243)
imshow(imx3)
subplot(247)
title(r'$\sigma=3$')
plot(range(len(img3[r])), img3[r])
plot(range(len(imx3[r])), imx3[r])

subplot(244)
imshow(imx4)
subplot(248)
title(r'$\sigma=4$')
plot(range(len(img4[r])), img4[r])
plot(range(len(imx4[r])), imx4[r])

show()