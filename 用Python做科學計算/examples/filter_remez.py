# -*- coding: utf-8 -*-
import scipy.signal as signal
import numpy as np
import pylab as pl

for length in [11, 31, 51, 101, 201]:
    b = signal.remez(length, (0, 0.18,  0.2,  0.50), (0.01, 1))
    w, h = signal.freqz(b, 1)
    pl.plot(w/2/np.pi, 20*np.log10(np.abs(h)), label=str(length))
pl.legend()
pl.xlabel(u"正规化频率 周期/取样")
pl.ylabel(u"幅值(dB)")
pl.title(u"remez设计高通滤波器 - 滤波器长度和频响的关系")
pl.show()

