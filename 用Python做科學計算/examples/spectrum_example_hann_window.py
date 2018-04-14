# -*- coding: utf-8 -*-
import pylab as pl
import scipy.signal as signal
pl.figure(figsize=(8,3))
pl.plot(signal.hann(512))
pl.title("hann window")
pl.xlim(0,511)
pl.show()