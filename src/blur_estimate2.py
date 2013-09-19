# -*- coding: utf-8 -*-
import os
import moojoos as mj
import numpy as np
import pylab as pyl
from PIL import Image
from scipy.ndimage import filters


#files = [ "rena_sharp.jpg", "rena_gaussian_2.jpg", "rena_gaussian_5.jpg", "rena_gaussian_10.jpg" ]
files = [ "rena_gaussian_10.jpg" ]
for fn in files:
    # obtain image
    cd = os.path.dirname(os.path.abspath(__file__))
    fp = os.path.join(cd, fn)

    # grayscale
    img = np.array(Image.open(fp).convert('L'))
    
    # smooth with median filter
    # TODO: make median filter size a parameter!
    #imm = filters.median_filter(img, 3)
    imm = img
    
    # calculate Sobel filters on median-smoothed image
    # to detect edges
    fsobx, fsoby = np.zeros(imm.shape), np.zeros(imm.shape)
    filters.sobel(imm, 1, fsobx)
    filters.sobel(imm, 0, fsoby)
    
    nbedges = 0
    totbm   = 0
    # IN the vertical direction...
    # FOR EACH row in the sobel-ized image
    #     identify all edge peaks
    #     increment edge counter
    #     FOR each edge peak in this row
    #         calculate width of edge
    #         increment local blur measure
    # calculate total blur measure for image rows
    for i in xrange(fsobx.shape[0]):
        mxs, mns = mj.signal.peak_detect(fsobx[i], lookahead=1, minpeak=5.0)
        maxx = mxs[0]
        minx = mns[0]
        epx  = list(set(maxx+minx))
        nbedges += len(epx)
        for p in epx:
            s,e = mj.signal.find_edge_startend(fsobx[i], p)
            totbm += (e-s)
    
    print "Image: %s" % fn
    print "Row blur"
    print "  nbedges detected: %d" % nbedges
    print "  acc. blur measure: %d" % totbm
    print "  blur measure: %f" % (totbm / (1.0*nbedges))
    print        
    
    # IN the horizontal   
    # FOR EACH col in the sobel-ized image
    #     identify all edge peaks
    #     
    foo = fsoby.transpose()
    nbedges = 0
    totbm   = 0
    for i in xrange(foo.shape[0]):
        mxs, mns = mj.signal.peak_detect(foo[i], lookahead=1, minpeak=5.0)
        maxx = mxs[0]
        minx = mns[0]
        epx  = list(set(maxx+minx))
        nbedges += len(epx)
        for p in epx:
            s,e = mj.signal.find_edge_startend(foo[i], p)
            totbm += (e-s)

    print "Col blur"
    print "  nbedges detected: %d" % nbedges
    print "  acc. blur measure: %d" % totbm
    print "  blur measure: %f" % (totbm / (1.0*nbedges))
    print 
    print