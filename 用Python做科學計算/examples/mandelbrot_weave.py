# -*- coding: utf-8 -*-

import numpy as np
import pylab as pl
import time
import scipy.weave as weave
from matplotlib import cm
    
def weave_iter_point(c):
    code = """
    std::complex<double> z;
    int i;
    z = c;
    for(i=1;i<100;i++) 
    {
        if(std::abs(z) > 2) break;
        z = z*z+c;
    }
    return_val=i;
    """
    
    f = weave.inline(code, ["c"], compiler="gcc")
    return f

def draw_mandelbrot(cx, cy, d,N=200):
    """
    绘制点(cx, cy)附近正负d的范围的Mandelbrot
    """
    x0, x1, y0, y1 = cx-d, cx+d, cy-d, cy+d 
    y, x = np.ogrid[y0:y1:N*1j, x0:x1:N*1j]
    c = x + y*1j
    start = time.clock()
    mandelbrot = np.frompyfunc(weave_iter_point,1,1)(c).astype(np.float)
    print "time=",time.clock() - start
    pl.imshow(mandelbrot, cmap=cm.Blues_r, extent=[x0,x1,y0,y1])
    pl.gca().set_axis_off()
    
x,y = 0.27322626, 0.595153338

pl.subplot(231)
draw_mandelbrot(-0.5,0,1.5)
for i in range(2,7):    
    pl.subplot(230+i)
    draw_mandelbrot(x, y, 0.2**(i-1))
pl.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0.02)

pl.show()