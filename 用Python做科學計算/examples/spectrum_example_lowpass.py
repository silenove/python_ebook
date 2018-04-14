# -*- coding: utf-8 -*-
import scipy.signal as signal
import numpy as np
import pylab as pl

def average_fft(x, fft_size):
    n = len(x) // fft_size * fft_size
    tmp = x[:n].reshape(-1, fft_size) 
    tmp *= signal.hann(fft_size, sym=0)
    xf = np.abs(np.fft.rfft(tmp)/fft_size)
    avgf = np.average(xf, axis=0)
    return 20*np.log10(avgf)

# 设计一个8kHz取样的1kHz的Chebyshev I低通滤波器
b,a=signal.iirdesign(1000/4000.0, 1100/4000.0, 1, -40, 0, "cheby1")
x = np.random.rand(100000) - 0.5
y = signal.filtfilt(b, a, x)

xf = average_fft(y, 512)
pl.figure(figsize=(7,3.5))
freqs = np.linspace(0, 4000, 257)
pl.plot(freqs, xf)
pl.title(u"经过低通滤波的白色噪声的频谱")
pl.xlabel(u"频率(Hz)")
pl.ylabel(u"幅值(dB)")
pl.subplots_adjust(bottom=0.15)
pl.show()
