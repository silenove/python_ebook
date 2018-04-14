# -*- coding: utf-8 -*-
import scipy.signal as signal
import numpy as np
import pylab as pl

h1 = signal.remez(201, (0, 0.18,  0.2,  0.50), (0.01, 1))
h2 = signal.remez(201, (0, 0.38,  0.4,  0.50), (1, 0.01))
h3 = np.convolve(h1, h2)

w, h = signal.freqz(h3, 1)
pl.plot(w/2/np.pi, 20*np.log10(np.abs(h)))

pl.legend()
pl.xlabel(u"正规化频率 周期/取样")
pl.ylabel(u"幅值(dB)")
pl.title(u"低通和高通级联为带通滤波器")
pl.show()
