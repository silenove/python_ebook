# -*- coding: utf-8 -*-
from sympy import *
from sympy import Derivative as D

var("x1 x2 y1 y2 l1 l2 m1 m2 th1 th2 dth1 dth2 ddth1 ddth2 t g tmp")

sublist = [
(D(th1(t), t, t), ddth1),
(D(th1(t), t), dth1),
(D(th2(t), t, t), ddth2),
(D(th2(t),t), dth2),
(th1(t), th1),
(th2(t), th2)    
]

x1 = l1*sin(th1(t))
y1 = -l1*cos(th1(t))
x2 = l1*sin(th1(t)) + l2*sin(th2(t))
y2 = -l1*cos(th1(t)) - l2*cos(th2(t))

vx1 = diff(x1, t)
vx2 = diff(x2, t)
vy1 = diff(y1, t)
vy2 = diff(y2, t)

# 拉格朗日量
L = m1/2*(vx1**2 + vy1**2) + m2/2*(vx2**2 + vy2**2) - m1*g*y1 - m2*g*y2

# 拉格朗日方程
def lagrange_equation(L, v):    
    a = L.subs(D(v(t), t), tmp).diff(tmp).subs(tmp, D(v(t), t))
    b = L.subs(D(v(t), t), tmp).subs(v(t), v).diff(v).subs(v, v(t)).subs(tmp, D(v(t), t))
    c = a.diff(t) - b
    c = c.subs(sublist)  
    c = trigsimp(simplify(c))
    c = collect(c, [th1,th2,dth1,dth2,ddth1,ddth2])
    return c

eq1 = lagrange_equation(L, th1)
eq2 = lagrange_equation(L, th2)