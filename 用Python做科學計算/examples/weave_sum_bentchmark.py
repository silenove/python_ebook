# -*- coding: utf-8 -*-
import scipy.weave as weave
import numpy as np
import time

def my_sum(a):
    n=int(len(a))
    code="""
    int i;

    double counter;
    counter =0;
    for(i=0;i<n;i++){
        counter=counter+a(i);
    }
    return_val=counter;
    """

    err=weave.inline(
        code,['a','n'],
        type_converters=weave.converters.blitz,
        compiler="gcc"
    )
    return err

a = np.arange(0, 10000000, 1.0)
# 先调用一次my_sum，weave会自动对C语言进行编译，此后直接运行编译之后的代码
my_sum(a)

start = time.clock()
for i in xrange(100):
    my_sum(a)  # 直接运行编译之后的代码
print "my_sum:", (time.clock() - start) / 100.0

start = time.clock()
for i in xrange(100):
    np.sum( a ) # numpy中的sum，其实现也是C语言级别
print "np.sum:", (time.clock() - start) / 100.0

start = time.clock()
print sum(a) # Python内部函数sum通过数组a的迭代接口访问其每个元素，因此速度很慢
print "sum:", time.clock() - start
