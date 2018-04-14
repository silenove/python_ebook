# -*- coding: utf-8 -*-
import numpy as np
from scipy import integrate

def half_circle(x):
    return (1-x**2)**0.5
    
def rect_integrate(N):
    x = np.linspace(-1, 1, N)
    dx = 2.0/N
    y = half_circle(x)
    return dx * np.sum(y[:-1] + y[1:]) * 0.5
    
def trazp_integrate(N):
    x = np.linspace(-1, 1, N)
    dx = 2.0/N
    y = half_circle(x)
    return np.trapz(y, x)
    
print rect_integrate(10000)*2
print trazp_integrate(10000)*2

pi_half, err = integrate.quad(half_circle, -1, 1)
print pi_half * 2

def half_sphere(x, y):
    return (1-x**2-y**2)**0.5
    
print integrate.dblquad(half_sphere, -1, 1, lambda x:-half_circle(x), lambda x:half_circle(x))