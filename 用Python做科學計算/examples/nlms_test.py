# -*- coding: utf-8 -*-
# filename: nlms_test.py

import numpy as np
import pylab as pl
import nlms_numpy
import scipy.signal


# 随机产生FIR滤波器的系数，长度为length， 延时为delay， 指数衰减
def make_path(delay, length):
   path_length = length - delay
   h = np.zeros(length, np.float64)
   h[delay:] = np.random.standard_normal(path_length) * np.exp( np.linspace(0, -4, path_length) )
   h /= np.sqrt(np.sum(h*h))
   return h

def plot_converge(y, u, label=""):
    size = len(u)
    avg_number = 200
    e = np.power(y[:size] - u, 2)
    tmp = e[:int(size/avg_number)*avg_number]
    tmp.shape = -1, avg_number
    avg = np.average( tmp, axis=1 )
    pl.plot(np.linspace(0, size, len(avg)), 10*np.log10(avg), linewidth=2.0, label=label)

def diff_db(h0, h):
   return 10*np.log10(np.sum((h0-h)*(h0-h)) / np.sum(h0*h0))    

# 用NLMS进行系统辨识的模拟, 未知系统的传递函数为h0, 使用的参照信号为x
def sim_system_identify(nlms, x, h0, step_size, noise_scale):
      y = np.convolve(x, h0)
      d = y + np.random.standard_normal(len(y)) * noise_scale # 添加白色噪声的外部干扰
      h = np.zeros(len(h0), np.float64) # 自适应滤波器的长度和未知系统长度相同，初始值为0
      u = nlms( x, d, h, step_size )
      return y, u, h

def system_identify_test1():
    h0 = make_path(32, 256) # 随机产生一个未知系统的传递函数
    x = np.random.standard_normal(10000)  # 参照信号为白噪声      
    y, u, h = sim_system_identify(nlms_numpy.nlms, x, h0, 0.5, 0.1)
    print diff_db(h0, h)
    pl.figure( figsize=(8, 6) )
    pl.subplot(211)
    pl.subplots_adjust(hspace=0.4)
    pl.plot(h0, c="r")
    pl.plot(h, c="b")
    pl.title(u"未知系统和收敛后的滤波器的系数比较")
    pl.subplot(212)
    plot_converge(y, u)
    pl.title(u"自适应滤波器收敛特性")
    pl.xlabel("Iterations (samples)")
    pl.ylabel("Converge Level (dB)")    
    pl.show()

def system_identify_test2():
    h0 = make_path(32, 256) # 随机产生一个未知系统的传递函数
    x = np.random.standard_normal(20000)  # 参照信号为白噪声   
    pl.figure(figsize=(8,4))
    for step_size in np.arange(0.1, 1.0, 0.2):
        y, u, h = sim_system_identify(nlms_numpy.nlms, x, h0, step_size, 0.1)
        plot_converge(y, u, label=u"μ=%s" % step_size)
    pl.title(u"更新系数和收敛特性的关系")
    pl.xlabel("Iterations (samples)")
    pl.ylabel("Converge Level (dB)")        
    pl.legend()
    pl.show()   

def system_identify_test3():
    h0 = make_path(32, 256) # 随机产生一个未知系统的传递函数
    x = np.random.standard_normal(20000)  # 参照信号为白噪声   
    pl.figure(figsize=(8,4))
    for noise_scale in [0.05, 0.1, 0.2, 0.4, 0.8]:
        y, u, h = sim_system_identify(nlms_numpy.nlms, x, h0, 0.5, noise_scale)
        plot_converge(y, u, label=u"noise=%s" % noise_scale)
    pl.title(u"外部干扰和收敛特性的关系")
    pl.xlabel("Iterations (samples)")
    pl.ylabel("Converge Level (dB)")        
    pl.legend()
    pl.show()       

def sim_signal_equation(nlms, x, h0, D, step_size, noise_scale):
    d = x[:-D]
    x = x[D:]
    y = np.convolve(x, h0)[:len(x)]
    h = np.zeros(2*len(h0)+2*D, np.float64)
    y += np.random.standard_normal(len(y)) * noise_scale    
    u = nlms(y, d, h, step_size)
    return h

def signal_equation_test1():    
    h0 = make_path(5, 64)
    D = 128
    length = 20000
    data = np.random.standard_normal(length+D)
    h = sim_signal_equation(nlms_numpy.nlms, data, h0, D, 0.5, 0.1)
    pl.figure(figsize=(8,4))
    pl.plot(h0, label=u"未知系统")
    pl.plot(h, label=u"自适应滤波器")
    pl.plot(np.convolve(h0, h), label=u"二者卷积")
    pl.title(u"信号均衡演示")
    pl.legend()
    w0, H0 = scipy.signal.freqz(h0, worN = 1000)
    w, H = scipy.signal.freqz(h, worN = 1000)
    pl.figure(figsize=(8,4))
    pl.plot(w0, 20*np.log10(np.abs(H0)), w, 20*np.log10(np.abs(H)))
    pl.title(u"未知系统和自适应滤波器的振幅特性")
    pl.xlabel(u"圆频率")
    pl.ylabel(u"振幅(dB)") 
    pl.show()
    
signal_equation_test1()
