# -*- coding: utf-8 -*-
import scipy.signal as signal
import numpy as np
import pylab as pl

for weight in [(1,1), (1, 0.1), (1, 0.01)]:
    b = signal.remez(101, (0, 0.18,  0.2,  0.50), (0.01, 1), weight=weight)
    w, h = signal.freqz(b, 1)
    pl.plot(w/2/np.pi, 20*np.log10(np.abs(h)), label="%s,%s"%(weight))
pl.legend()
pl.xlabel(u"正规化频率 周期/取样")
pl.ylabel(u"幅值(dB)")
pl.title(u"remez设计高通滤波器 - 权值和频响的关系")
pl.show()

