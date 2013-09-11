# -*- coding: utf-8 -*-
import os

from numpy import *
from PIL import Image
from pylab import *
from scipy.ndimage import filters
from peakdetect import *


def find_edge_startend(arr, peak):
    def _find_edge(arr, start, inc=1):
        if start == len(arr)-1:
            return start
        elif start == len(arr)-2:
            return start+1
        else:
            while True:
                p1 = start+inc
                p2 = p1+inc
                d1 = arr[start]-arr[p1]
                d2 = arr[p1]-arr[p2]
                if d1 >= arr[start]:
                    return p1
                elif d1*d2 < 0:
                    return p1
                else:
                    start += inc
            
    start = _find_edge(arr, peak, -1)
    end   = _find_edge(arr, peak)
        
    return start, end     
            


cd = os.path.dirname(os.path.abspath(__file__))
fn = "test3.jpg"
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
a, b = peakdetect(fsobx[r], lookahead=1)
a = zip(*a)
b = zip(*b)
maxx, maxy = a[0], a[1]
minx, miny = b[0], b[1]

print maxx, maxy
print minx, miny

# detect peaks in Sobel horiz
aa, bb = peakdetect(fsoby[:,c], lookahead=1)
aa = zip(*aa)
bb = zip(*bb)
maxx2, maxy2 = aa[0], aa[1]
minx2, miny2 = bb[0], bb[1]

print maxx2, maxy2
print minx2, miny2

figure()
gray()

subplot(221)
title("Sobel, vert")
imshow(fsobx) 
axhline(r, lw=0.5, color='b', ls=':')
for pk in [87, 117, 145]:
    s,e = find_edge_startend(fsobx[r], pk)
    plot(s, r, 'r+')
    plot(e, r, 'r+')

subplot(222)
title("Sobel, horiz")
imshow(fsoby) 
axvline(c, lw=0.5, color='b', ls=':')
for pk in [25, 54, 85]:
    s,e = find_edge_startend(fsoby[:,c], pk)
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