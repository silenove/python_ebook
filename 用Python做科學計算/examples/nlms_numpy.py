# -*- coding: utf-8 -*-
# filename: nlms_numpy.py

import numpy as np

# 用Numpy实现的NLMS算法
# x为参照信号，d为目标信号，h为自适应滤波器的初值
# step_size为更新系数
def nlms(x, d, h, step_size=0.5):
   i = len(h)
   size = len(x)
   # 计算输入到h中的参照信号的乘方he
   power = np.sum( x[i:i-len(h):-1] * x[i:i-len(h):-1] )
   u = np.zeros(size, dtype=np.float64)

   while True:
       x_input = x[i:i-len(h):-1]
       u[i] = np.sum(x_input * h)
       e = d[i] - u[i]
       h += step_size * e * x_input / power

       power -= x_input[-1] * x_input[-1] # 减去最早的取样
       i+=1
       if i >= size: return u
       power += x[i] * x[i] # 增加最新的取样
