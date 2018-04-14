# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
t = np.arange(0, 1.0, 1.0/8000)
x = np.sin(2*np.pi*50*t)[:512]
pl.figure(figsize=(8,3))
pl.plot(np.hstack([x,x,x]))
pl.title(u"50Hz正弦波的512点FFT所计算的频谱的实际波形")
pl.xlabel(u"取样点")
pl.subplots_adjust(bottom=0.15)
pl.show()