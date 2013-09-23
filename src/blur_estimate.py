# -*- coding: utf-8 -*-
import os
import moojoos as mj
import numpy as np

from pylab import *
from PIL import Image
from scipy.ndimage import filters

# target files for comparison
files = [ 'rena_sharp.jpg', 'rena_gaussian_2.jpg' ]

# targetting rena's lips?
r = 260

cd = os.path.dirname(os.path.abspath(__file__))

# gray-scaled images
test1 = np.array(Image.open(os.path.join(cd, files[0])).convert('L'))
test2 = np.array(Image.open(os.path.join(cd, files[1])).convert('L'))

# median-filtered: does noise-reduction help later calculations???
t1_med = filters.median_filter(test1, 3)
t2_med = filters.median_filter(test2, 3)

# Sobel filters
t1_sob, t1_sobm = np.zeros(test1.shape), np.zeros(test1.shape)
t2_sob, t2_sobm = np.zeros(test2.shape), np.zeros(test2.shape)
filters.sobel(test1,  1, t1_sob)     # Sobel, vert. on orig. gray-scale image
filters.sobel(test2,  1, t2_sob)     
filters.sobel(t1_med, 1, t1_sobm)    # Sobel, vert. on median-filtered image
filters.sobel(t2_med, 1, t2_sobm) 

# Edge markers @ r
t1s_mx, t1s_mn = mj.signal.peak_detect(t1_sob[r], lookahead=1, minpeak=4.0)
t1s_peaks  = list(set(t1s_mx[0]+t1s_mn[0]))
t1sm_mx, t1sm_mn = mj.signal.peak_detect(t1_sobm[r], lookahead=1, minpeak=4.0)
t1sm_peaks = list(set(t1sm_mx[0]+t1sm_mn[0]))

t2s_mx, t2s_mn = mj.signal.peak_detect(t2_sob[r], lookahead=1, minpeak=4.0)
t2s_peaks  = list(set(t2s_mx[0]+t2s_mn[0]))
t2sm_mx, t2sm_mn = mj.signal.peak_detect(t2_sobm[r], lookahead=1, minpeak=4.0)
t2sm_peaks = list(set(t2sm_mx[0]+t2sm_mn[0]))

figure()
gray()

###############################################################################
subplot(4,3,1)
title('rena, sharp')
imshow(test1)
axis('off')

subplot(4,3,2)
imshow(t1_sob)
xlim(0,test1.shape[1])
ylim(test1.shape[0],0)
xticks(range(0,350,100))
for p in t1s_peaks:
    s,e = mj.signal.find_edge_startend(t1_sob[r], p)
    plot(s, r, 'b+')
    plot(e, r, 'g+')

subplot(4,3,3)
ylim(-600,1000)
plot(range(len(test1[r])), test1[r])
plot(range(len(t1_sob[r])), t1_sob[r])
axhline(y=0, color='green', ls='--')
plot(t1s_peaks, t1_sob[r][t1s_peaks], 'r+')

###############################################################################
subplot(4,3,4)
title('rena, sharp - med.filt.')
imshow(t1_med)
axis('off')

subplot(4,3,5)
imshow(t1_sobm)
xlim(0,t1_sobm.shape[1])
ylim(t1_sobm.shape[0],0)
xticks(range(0,350,100))
for p in t1sm_peaks:
    s,e = mj.signal.find_edge_startend(t1_sobm[r], p)
    plot(s, r, 'b+')
    plot(e, r, 'g+')
    
subplot(4,3,6)
ylim(-600,1000)
plot(range(len(test1[r])), test1[r])
plot(range(len(t1_sobm[r])), t1_sobm[r])
axhline(y=0, color='green', ls='--')
plot(t1sm_peaks, t1_sobm[r][t1sm_peaks], 'r+')    
    
###############################################################################
subplot(4,3,7)
title('rena, blurred')
imshow(test2)
axis('off')

subplot(4,3,8)
imshow(t2_sob)
xlim(0,t2_sob.shape[1])
ylim(t2_sob.shape[0],0)
xticks(range(0,350,100))
for p in t2s_peaks:
    s,e = mj.signal.find_edge_startend(t2_sob[r], p)
    plot(s, r, 'b+')
    plot(e, r, 'g+')

subplot(4,3,9)
ylim(-600,1000)
plot(range(len(test2[r])), test2[r])
plot(range(len(t2_sob[r])), t2_sob[r])
axhline(y=0, color='green', ls='--')
plot(t2s_peaks, t2_sob[r][t2s_peaks], 'r+')
    
###############################################################################
subplot(4,3,10)
title('rena, blurred - med.filt.')
imshow(t2_med)
axis('off')

subplot(4,3,11)
imshow(t2_sobm)
xlim(0,test2.shape[1])
ylim(test2.shape[0],0)
xticks(range(0,350,100))
for p in t2sm_peaks:
    s,e = mj.signal.find_edge_startend(t2_sobm[r], p)
    plot(s, r, 'b+')
    plot(e, r, 'g+')
    
subplot(4,3,12)
ylim(-600,1000)
plot(range(len(test2[r])), test2[r])
plot(range(len(t2_sobm[r])), t2_sobm[r])
axhline(y=0, color='green', ls='--')
plot(t2sm_peaks, t2_sobm[r][t2sm_peaks], 'r+')    
    
#
#imx0 = zeros(imr.shape)
#filters.sobel(imr, 1, imx0)
#
#imx2 = zeros(imr.shape)
#filters.sobel(img2, 1, imx2)
#
#imx3 = zeros(imr.shape)
#filters.sobel(img3, 1, imx3)
#
#imx4 = zeros(imr.shape)
#filters.sobel(img4, 1, imx4)
#
#subplot(241)
#imshow(imx0)
#title('Untouched')
#subplot(245)
#plot(range(len(imr[r])), imr[r])
#plot(range(len(imx0[r])), imx0[r]) 
#
#subplot(242)
#imshow(imx2) 
#title(r'Gaussian, $\sigma=2$')
#subplot(246)
#plot(range(len(img2[r])), img2[r])
#plot(range(len(imx2[r])), imx2[r]) 
#
#subplot(243)
#imshow(imx3)
#title(r'Gaussian, $\sigma=3$')
#subplot(247)
#plot(range(len(img3[r])), img3[r])
#plot(range(len(imx3[r])), imx3[r])
#
#subplot(244)
#imshow(imx4)
#title(r'Gaussian, $\sigma=4$')
#subplot(248)
#plot(range(len(img4[r])), img4[r])
#plot(range(len(imx4[r])), imx4[r])
#
show()