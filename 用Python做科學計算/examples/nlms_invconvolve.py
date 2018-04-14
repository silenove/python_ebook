# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from nlms_numpy import nlms
import scipy.signal as signal

def inv_convolve(h1, h3, length):
    x = np.random.standard_normal(10000)
    u = signal.lfilter(h1, 1, x)
    d = signal.lfilter(h3, 1, x)
    h = np.zeros(length, np.float64)
    nlms(u, d, h, 0.1)
    return h

h1 = np.fromfile("h1.txt", sep="\n")
h1 /= np.max(h1)
h3 = np.fromfile("h3.txt", sep="\n")
h3 /= np.max(h3)

pl.rc('legend', fontsize=10)
pl.subplot(411)
pl.plot(h3, label="h3")
pl.plot(h1, label="h1")
pl.legend()
pl.gca().set_yticklabels([]) 
for idx, length in enumerate([128, 256, 512]):
    pl.subplot(412+idx)
    h2 = inv_convolve(h1, h3, length)
    pl.plot(np.convolve(h1, h2)[:len(h3)], label="h1*h2(%s)" % length)
    pl.legend()
    pl.gca().set_yticklabels([]) 
    pl.gca().set_xticklabels([]) 

pl.show()
