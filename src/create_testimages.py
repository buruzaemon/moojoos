# -*- coding: utf-8 -*-
import os

from PIL import Image
from scipy import misc
from scipy.ndimage import filters

cd = os.path.dirname(os.path.abspath(__file__))
fn = "rena_sharp"
fp = os.path.join(cd, fn+".jpg")

# transform raw image into grayscale
img = Image.open(fp).convert('L')

# next, create 3 copies of varying blurriness (Gaussian)
blur = [2, 5, 10]
for b in blur:
    gd = filters.gaussian_filter(img, b)
    misc.imsave("%s_%s.jpg" % (fn,b), gd)