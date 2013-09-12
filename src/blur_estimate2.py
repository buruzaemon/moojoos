# -*- coding: utf-8 -*-
import os

from numpy import *
from PIL import Image
from pylab import *
from scipy.ndimage import filters
import moojoos as mj

cd = os.path.dirname(os.path.abspath(__file__))
fn = "BlurryMink.jpg"
#fn = "test3.jpg"
fp = os.path.join(cd, fn)

# target row
r = 100
c = 50

# original image, grayscale
orig = array(Image.open(fp).convert('L'))

# Sobel filter to detect edges in the vertical
fsobx, fsoby = zeros(orig.shape), zeros(orig.shape)
filters.sobel(orig, 1, fsobx)
filters.sobel(orig, 0, fsoby)

# detect peaks in Sobel vert
a, b = mj.signal.peak_detect(fsobx[r], lookahead=2, minpeak=5.0)
maxx, maxy = a[0], a[1]
minx, miny = b[0], b[1]

# detect peaks in Sobel horiz
aa, bb = mj.signal.peak_detect(fsoby[:,c], lookahead=2, minpeak=5.0)
maxx2, maxy2 = aa[0], aa[1]
minx2, miny2 = bb[0], bb[1]


figure()
gray()

subplot(221)
title("Sobel, vert")
imshow(fsobx) 
axhline(r, lw=0.5, color='b', ls=':')
for pk in maxx+minx:
    s,e = mj.signal.find_edge_startend(fsobx[r], pk)
    plot(s, r, 'r+')
    plot(e, r, 'r+')

subplot(222)
title("Sobel, horiz")
imshow(fsoby) 
axvline(c, lw=0.5, color='b', ls=':')
for pk in maxx2+minx2:
    s,e = mj.signal.find_edge_startend(fsoby[:,c], pk)
    plot(c, s, 'r+')
    plot(c, e, 'r+')

subplot(223)
title("Vert Edges")
xlim(0, fsobx.shape[1])
plot(range(len(orig[r])), orig[r])
plot(range(len(fsobx[r])), fsobx[r]) 
plot(maxx, maxy, "r+")
plot(minx, miny, "r+")

subplot(224)
title("Horiz Edges")
plot(range(len(orig[:,c])), orig[:,c])
plot(range(len(fsoby[:,c])), fsoby[:,c]) 
plot(maxx2, maxy2, "r+")
plot(minx2, miny2, "r+")

show()