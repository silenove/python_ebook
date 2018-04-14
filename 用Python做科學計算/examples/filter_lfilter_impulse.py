# -*- coding: utf-8 -*-
import scipy.signal as signal
import numpy as np
import pylab as pl

# 某个均衡滤波器的参数
a = np.array([1.0, -1.947463016918843, 0.9555873701383931])
b = np.array([0.9833716591860479, -1.947463016918843, 0.9722157109523452])

# 44.1kHz， 1秒的频率扫描波
t = np.arange(0, 0.5, 1/44100.0)
x= signal.chirp(t, f0=10, t1 = 0.5, f1=1000.0)
y = signal.lfilter(b, a, x)
ns = range(10, 1100, 100)
err = []

for n in ns:
    # 计算脉冲响应
    impulse = np.zeros(n, dtype=np.float)
    impulse[0] = 1
    h = signal.lfilter(b, a, impulse)
    
    # 直接FIR滤波器的输出
    y2 = signal.lfilter(h, 1, x)
   
    # 输出y和y2之间的误差
    err.append(np.sum((y-y2)**2))

# 绘图
pl.figure(figsize=(8,4))
pl.semilogy(ns , err, "-o")
pl.xlabel(u"脉冲响应长度")
pl.ylabel(u"FIR模拟IIR的误差")
pl.show()