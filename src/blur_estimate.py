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
#imshow(imx2)
subplot(131)
title(r'$\sigma=2$')
plot(range(len(img2[r])), img2[r])

imx3 = zeros(imr.shape)
filters.sobel(img3, 1, imx3)
#imshow(imx3)
subplot(132)
title(r'$\sigma=3$')
plot(range(len(img3[r])), img3[r])

imx4 = zeros(imr.shape)
filters.sobel(img4, 1, imx4)
#imshow(imx4)
subplot(133)
title(r'$\sigma=4$')
plot(range(len(img4[r])), img4[r])

show()