# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
import matplotlib

matplotlib.rcParams["legend.fontsize"]="small"

def windowed_sinc(fc, M, K):
    i = np.arange(0,M,1.0)
    h = K * np.sin(2*np.pi*fc*(i-M/2.0))/(i-M/2.0)
    h *= 0.42 - 0.5*np.cos(2*np.pi*i/M) + 0.08*np.cos(4*np.pi*i/M)
    return h
    
x = np.random.rand(300) - 0.5   
h = windowed_sinc(0.05, 101, 1.0)

xs = []
for i in range(3):
    tmp = np.zeros(len(x), dtype=np.float64)
    tmp[i*100:i*100+100] = x[ i*100:i*100+100 ]
    xs.append(tmp)

y = np.convolve(x,h)
fig = pl.figure(figsize=(8,16))

pl.subplot(521)
pl.plot(x, label=u"原始信号x")
pl.gca().set_yticklabels([])
pl.gca().set_xticklabels([])
pl.legend()

pl.subplot(522)
pl.plot(h, label=u"滤波器系数h")
pl.gca().set_yticklabels([])
pl.gca().set_xticklabels([])
pl.legend()

result = []
for i,tmp in enumerate(xs):
    pl.subplot(520+3+i*2)
    pl.plot(tmp, label=u"分段%s" % (i+1))
    pl.gca().set_yticklabels([])
    pl.gca().set_xticklabels([])
    pl.legend()
    pl.subplot(520+3+i*2+1)
    tmp = np.convolve(tmp, h)
    result.append(tmp)
    pl.plot(tmp, label=u"分段卷积%s" % (i+1))
    pl.gca().set_yticklabels([])
    pl.gca().set_xticklabels([])  
    pl.axvspan(i*100,i*100+200,alpha=0.3,facecolor="g")
    pl.legend()

pl.subplot(529)
pl.plot(np.convolve(x,h), label=u"原始信号卷积")
pl.gca().set_yticklabels([])
pl.gca().set_xticklabels([])  
pl.legend()

pl.subplot(5,2,10)
pl.plot(np.sum(result, axis=0), label=u"分段卷积和")
pl.gca().set_yticklabels([])
pl.gca().set_xticklabels([]) 
pl.legend()

pl.subplots_adjust(hspace=0.05, wspace=0.03, top=0.95, bottom=0.01,left=0.03,right=0.97)
pl.figtext(0.5, 0.965,  u"分段卷积演示",
           ha='center', color='black', weight='bold', size='large')
pl.show()