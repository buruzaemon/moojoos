# -*- coding: utf-8 -*-
import os
import moojoos as mj
import numpy as np

from pylab import *
from PIL import Image
from scipy.ndimage import filters

# target files for comparison
files = [ 'rena_sharp.jpg', 'rena_gaussian_2.jpg' ]

cd = os.path.dirname(os.path.abspath(__file__))

# gray-scaled images
test1 = np.array(Image.open(os.path.join(cd, files[0])).convert('L'))
test2 = np.array(Image.open(os.path.join(cd, files[1])).convert('L'))

## targetting rena's lips?
#r = 260

t1_sob = np.zeros(test1.shape)
filters.sobel(test1,  1, t1_sob) 

figure()
gray()

#for r in xrange(test1.shape[0]):
for r in [260]:
    t1s_mx, t1s_mn = mj.signal.peak_detect(t1_sob[r], lookahead=1, minpeak=4.0)
    t1s_peaks  = list(set(t1s_mx[0]+t1s_mn[0]))
    
    for p in t1s_peaks:
        s,e = mj.signal.find_edge_startend(t1_sob[r], p)        
        plot(e-s, np.abs(p), 'g+')
show()