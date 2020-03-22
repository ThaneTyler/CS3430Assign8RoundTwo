#!/usr/bin/python

#######################################################
# module: cs3430_s20_hw08.py
# Thane Tyler
# A01819635
########################################################

import math
from PIL import Image
import numpy as np

def lumin(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    """
    Convert rgb pixel to grayscale value.
    """
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

def is_in_pil_range(pil_img, cr):
    """
    Check if 2-tuple cr references to a legal pixel in a PIl image pil_img
    """
    ncols, nrows = pil_img.size
    c, r = cr
    #print('ncols={}; nrows={}'.format(ncols, nrows))
    #print('c={}; r={}'.format(c, r))
    return c > 0 and c < ncols-1 and r > 0 and r < nrows-1

def display_pil_img_row(pil_img, r):
    """
    Prints pixel values in row r in a PIL image pil_img.
    Useful for debugging.
    """
    ncols, _ = pil_img.size
    for c in range(ncols):
        print(pil_img.getpixel((c, r)))

def display_pil_img_col(pil_img, c):
    """
    Prints pixel values in column c in a PIL image pil_img.
    Useful for debugging.
    """
    _, nrows = pil_img.size
    for r in range(nrows):
        print(pil_img.getpixel((c, r)))

### ================ Problem 01 =================================

## Remember: in PIL images, c = x, r = y
def pil_pix_dxdy(pil_img, cr, default_delta):
    """
    Returns dx, dy values for pixel (c, r) in PIL image pil_img.
    If the luminosity values of the horizontal neighbors are the same,
    dx = default_delta.
    If the luminosity values of the vertical neighbors are the same,
    dy = default_delta.
    """
    assert is_in_pil_range(pil_img, cr)
    if ( lumin(pil_img.getpixel((cr[0], cr[1] - 1))) != lumin(pil_img.getpixel((cr[0], cr[1] + 1))) ):
        dy = ( lumin(pil_img.getpixel((cr[0], cr[1] - 1))) - lumin(pil_img.getpixel((cr[0], cr[1] + 1))) )
    else:
        dy = default_delta

    if ( lumin(pil_img.getpixel((cr[0] + 1, cr[1]))) != lumin(pil_img.getpixel((cr[0] - 1, cr[1]))) ):
        dx = (lumin(pil_img.getpixel((cr[0] + 1, cr[1]))) - lumin(pil_img.getpixel((cr[0] - 1, cr[1]))))
    else:
        dx = default_delta

    return dx, dy

def grd_magn(dx, dy):
    """
    Gradient magnitude given dx and dy. Given by pil_pix_dxdy
    """
    ## your code here
    pass

def grd_deg_theta(dx, dy):
    """
    Gradient orientation (in degrees) given dx and dy.
    """
    ## your code here
    pass

def depil(pil_img, default_delta=1.0, magn_thresh=20):
    """
    - detects edges in a PIL image pil_img.
    - returns a new binary PIL image where the pixel
    value 255 means that it's a edge pixel and 0 means
    that it's not an edge pixel.
    - default_delta is used in calls to pil_pix_dxdy
    - magn_thresh is a gradient magnitude threshold, i.e.,
    if the computed value is >= magn_thresh, the pixel
    is an edge pixel; otherwise, it's not.
    """
    output_img = Image.new('L', pil_img.size)
    num_cols, num_rows = pil_img.size
    ## your code here
    return output_img

### ================ Problem 02 =================================

def ht(pil_img, angle_step=1, pix_val_thresh=5):
    ## your code here
    pass

def ht_find_lines(htb, spl=1):
    """
    - Returns a list of all lines in the hough transform table htb if
    with rhos >= 0 and support level >= spl.
    - Each line is represented as a 3-tuple (rho, angle, spl), 
    where angle is given in degrees.
    """
    ## your code here
    pass


