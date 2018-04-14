# -*- coding: utf-8 -*-
from scipy.optimize import fsolve
from math import sin,cos
def f(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [
        5*x1+3,
        4*x0*x0 - 2*sin(x1*x2),
        x1*x2 - 1.5
    ]
    
def j(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])    
    return [
        [0, 5, 0],
        [8*x0, -2*x2*cos(x1*x2), -2*x1*cos(x1*x2)],
        [0, x2, x1]
    ]
 
result = fsolve(f, [1,1,1], fprime=j)
print result
print f(result)
