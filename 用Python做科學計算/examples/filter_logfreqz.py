# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
import scipy.signal as signal

def logfreqz(b, a, f0, f1, fs, N):
    """
    以对数频率坐标计算滤波器b,a的频率响应
    f0, f1: 计算频率响应的开始频率和结束频率
    fs: 取样频率
    """
    w0, w1 = np.log10(f0/fs*2*np.pi), np.log10(f1/fs*2*np.pi)
    # 不包括结束频率
    w = np.logspace(w0, w1, N, endpoint=False)
    zm1 = np.exp(-1j*w)
    h = np.polyval(b[::-1], zm1) / np.polyval(a[::-1], zm1)
    return w/2/np.pi*fs, h
    
for n in range(1, 6):    
    # 设计n阶的通频为0.1*4000 = 400Hz的低通滤波器
    b, a = signal.iirfilter(n, [0.1, 1])    
    f, h = logfreqz(b, a, 10.0, 4000.0, 8000.0, 400)
    gain = 20*np.log10(np.abs(h))
    pl.semilogx(f, gain, label="N=%s" % n)
    slope = (gain[100]-gain[10]) / (np.log2(f[100]) - np.log2(f[10]))
    print "N=%s, slope=%s dB" % (n, slope)
pl.ylim(-100, 20)
pl.xlabel(u"频率(Hz)")
pl.ylabel(u"增益(dB)")
pl.legend()
pl.show()