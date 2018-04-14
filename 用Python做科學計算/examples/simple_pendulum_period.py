# -*- coding: utf-8 -*-
from math import sin, sqrt
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve
import pylab as pl
from scipy.special import ellipk

g = 9.8

def pendulum_equations(w, t, l):
    th, v = w
    dth = v
    dv  = - g/l * sin(th)
    return dth, dv

def pendulum_th(t, l, th0):
    track = odeint(pendulum_equations, (th0, 0), [0, t], args=(l,))
    return track[-1, 0]
    
def pendulum_period(l, th0):
    t0 = 2*np.pi*sqrt( l/g ) / 4
    t = fsolve( pendulum_th, t0, args = (l, th0) )
    return t*4
    
ths = np.arange(0, np.pi/2.0, 0.01)
periods = [pendulum_period(1, th) for th in ths]
periods2 = 4*sqrt(1.0/g)*ellipk(np.sin(ths/2)**2) # 计算单摆周期的精确值
pl.plot(ths, periods, label = u"fsolve计算的单摆周期", linewidth=4.0)
pl.plot(ths, periods2, "r", label = u"单摆周期精确值", linewidth=2.0)
pl.legend(loc='upper left')
pl.title(u"长度为1米单摆：初始摆角-摆动周期")
pl.xlabel(u"初始摆角(弧度)")
pl.ylabel(u"摆动周期(秒)")
pl.show()
