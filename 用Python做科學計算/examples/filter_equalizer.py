# -*- coding: utf-8 -*-

import scipy.signal as signal
import pylab as pl
import math
import numpy as np

def design_equalizer(freq, Q, gain, Fs):
    '''设计二次均衡滤波器的系数'''
    A = 10**(gain/40.0)
    w0 = 2*math.pi*freq/Fs
    alpha = math.sin(w0) / 2 / Q
    
    b0 = 1 + alpha * A
    b1 = -2*math.cos(w0)
    b2 = 1 - alpha * A
    a0 = 1 + alpha / A
    a1 = -2*math.cos(w0)
    a2 = 1 - alpha / A
    return [b0/a0,b1/a0,b2/a0], [1.0, a1/a0, a2/a0]    
    
pl.figure(figsize=(8,4))
for freq in [1000, 2000, 4000]:  
    for q in [0.5, 1.0]:
        for p in [5, -5, -10]:
            b,a = design_equalizer(freq, q, p, 44100)
            w, h = signal.freqz(b, a)
            pl.semilogx(w/np.pi*44100, 20*np.log10(np.abs(h)))
pl.xlim(100, 44100)      
pl.xlabel(u"频率(Hz)")
pl.ylabel(u"振幅(dB)")
pl.subplots_adjust(bottom=0.15)
pl.show()
