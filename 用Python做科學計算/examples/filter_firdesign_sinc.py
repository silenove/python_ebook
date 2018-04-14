# -*- coding: utf-8 -*-
import scipy.signal as signal
import numpy as np
import pylab as pl

def h_ideal(n, fc):
    return 2*fc*np.sinc(2*fc*np.arange(-n, n, 1.0))

b = h_ideal(30, 0.25)

w, h = signal.freqz(b)

pl.figure(figsize=(8,3))
pl.plot(w/2/np.pi, 20*np.log10(np.abs(h)))
pl.xlabel(u"正规化频率 周期/取样")
pl.ylabel(u"幅值(dB)")
pl.show()