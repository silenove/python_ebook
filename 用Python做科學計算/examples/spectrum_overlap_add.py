# -*- coding: utf-8 -*-
import numpy as np
x = np.random.rand(1000)
h = np.random.rand(101)
y = np.convolve(x, h)

N = 50 # 分段大小
M = len(h) # 滤波器长度

output = []

#缓存初始化为0
buffer = np.zeros(M+N-1,dtype=np.float64)

for i in xrange(len(x)/N):
    #从输入信号中读取N个数据
    xslice = x[i*N:(i+1)*N]
    #计算卷积
    yslice = np.convolve(xslice, h)
    #将卷积的结果加入到缓冲中
    buffer += yslice
    #输出缓存中的前N个数据，注意使用copy，否则输出的是buffer的一个视图
    output.append( buffer[:N].copy() )
    #缓存中的数据左移动N个元素
    buffer[0:M-1] = buffer[N:]
    #后面的补0
    buffer[M-1:] = 0

#将输出的数据组合为数组
y2 = np.hstack(output)
#计算和直接卷积的结果之间的误差
print np.sum(np.abs( y2 - y[:len(x)] ) )
