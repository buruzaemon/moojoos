# -*- coding: utf-8 -*-
import os
import moojoos as mj
import numpy as np
import pylab as pyl
from PIL import Image
from scipy.ndimage import filters


# obtain image
cd = os.path.dirname(os.path.abspath(__file__))
#fn = "rena_sharp.jpg"
#fn = "rena_gaussian_2.jpg"
#fn = "rena_gaussian_5.jpg"
fn = "rena_gaussian_10.jpg"
fp = os.path.join(cd, fn)

# grayscale
img = np.array(Image.open(fp).convert('L'))

# smooth with median filter
# TODO: make median filter size a parameter!
imm = filters.median_filter(img, 3)

# calculate Sobel filters on median-smoothed image
# to detect edges
fsobx, fsoby = np.zeros(imm.shape), np.zeros(imm.shape)
filters.sobel(imm, 1, fsobx)
filters.sobel(imm, 0, fsoby)

# TODO: make lookahead and minpeak parameters!
# IN the vertical direction...
#     FOR EACH row in the sobel-ized image
#         identify all edge pixels
#     FOR each edge pixel in this row
#         calculate difference of differences
#         calculate estimated contrast
#         calculate sharpness measure
#             IFF measured sharpness exceeds threshold
#                 increment sharp pixel count
#             increment total edge pixel count for x
#  calculate total sharpness for R_x
r_x = 0.0
p_x = 0

e_x_vals = []

for i in xrange(fsobx.shape[0]):
    mxs, mns = mj.signal.peak_detect(fsobx[i], lookahead=1, minpeak=5.0)
    maxx = mxs[0]
    minx = mns[0]
    epx  = list(set(maxx+minx))
    
    epxi = []
    for p in epx:
        s,e = mj.signal.find_edge_startend(fsobx[i], p)
        epxi.extend(np.arange(s,e+1))
    epxi = list(set(epxi))
    for i in epxi:
        e_x_vals.append(mj.blur.sharpness(img[i], e, 5))


#val = []
#for e in epxi:
#    val.append( mj.blur.sharpness(img[100], e, 5) )

#print val
#pyl.hist(val, 200, normed=1, histtype='stepfilled')

# IN the horizontal direction...
#     FOR EACH column in the sobel-ized image
#         identify all edge pixels
#         FOR each edge pixel in this column
#             calculate difference of differences
#             calculate estimated contrast
#             calculate sharpness measure
#             IFF measured sharpness exceeds threshold
#                 increment sharp pixel count
#             increment total edge pixel count for y
#  calculate total sharpness for R_y
#r_y = 0.0
#
## calculate overall sharpness as S_i = sqrt(R_x**2 + R_y**2) / sqrt(2)
#s_i = np.sqrt(np.square(r_x) + np.square(r_y)) / np.sqrt(2.0)
#
## calculate overall blur as 1 - S_i
#print "Estimated total blur: %f" % (1.0 - s_i)
#
#pyl.figure()
#pyl.gray()
#
#pyl.subplot(221)
#pyl.imshow(img) 
#pyl.title('Original image, grayscale')
#pyl.axis('off')
#
#pyl.subplot(222)
#pyl.imshow(imm) 
#pyl.title('Image, median-filtered')
#pyl.axis('off')
#
#pyl.subplot(223)
#pyl.imshow(fsobx) 
#pyl.title('Sobel, vert edges')
#
#pyl.subplot(224)
#pyl.imshow(fsoby) 
#pyl.title('Sobel, horiz edges')
#
#pyl.show()