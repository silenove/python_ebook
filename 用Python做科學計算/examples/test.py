# -*- coding: utf-8 -*-
class A(object):
    def __init__(self):
        self.__X = 3
        
class B(A):
    def __init__(self):
        A.__init__(self)
        self.__X = 4
        
    def test(self):
        self.__Y = 7
        
from scipy.fftpack import convolve     

def kernel(k):
    if k>0: return 1.0
    elif k<0: return -1.0
    return 0.0
    
x = np.arange(8)
y = fftpack.hilbert(x)
h = 2/np.pi/(np.arange(8)+1)
h[1::2] = 0