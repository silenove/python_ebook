# -*- coding: utf-8 -*-

import numpy as np
import pylab as pl
from math import log
from matplotlib import cm

escape_radius = 10
iter_num = 20

def smooth_iter_point(c):
    z = c
    for i in xrange(1, iter_num): 
        if abs(z)>escape_radius: break 
        z = z*z+c
    absz = abs(z)
    if absz > 2.0:
        mu = i - log(log(abs(z),2),2)
    else:
        mu = i
    return mu # 返回正规化的迭代次数
    
def iter_point(c):
    z = c
    for i in xrange(1, iter_num):
        if abs(z)>escape_radius: break 
        z = z*z+c
    return i
    
def draw_mandelbrot(cx, cy, d, N=200):
    global mandelbrot
    """
    绘制点(cx, cy)附近正负d的范围的Mandelbrot
    """
    x0, x1, y0, y1 = cx-d, cx+d, cy-d, cy+d 
    y, x = np.ogrid[y0:y1:N*1j, x0:x1:N*1j]
    c = x + y*1j
    mand = np.frompyfunc(iter_point,1,1)(c).astype(np.float)
    smooth_mand = np.frompyfunc(smooth_iter_point,1,1)(c).astype(np.float)
    pl.subplot(121)
    pl.gca().set_axis_off()
    pl.imshow(mand, cmap=cm.Blues_r, extent=[x0,x1,y0,y1])
    pl.subplot(122)    
    pl.imshow(smooth_mand, cmap=cm.Blues_r, extent=[x0,x1,y0,y1])
    pl.gca().set_axis_off()
    
draw_mandelbrot(-0.5,0,1.5,300)
pl.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)
pl.show()
