# -*- coding: utf-8 -*-
import numpy as np

class LatticeFilter(object):
    def __init__(self, M):
        self.f = np.zeros(M+1, np.float)
        self.b = np.zeros(M+1, np.float)
        self.lb = np.zeros(M, np.float)
        
        self.rb = np.zeros(M, np.float)
        self.rf = np.zeros(M, np.float)
        
    def input(self, x):
        self.f[0] = x
        np.multiply(self.lb, self.rf, self.f[1:])
        np.multiply(self.f[1:], -1, self.f[1:])
        np.add.accumulate(self.f, out = self.f)
        
        np.multiply(self.f[:-1], self.rb, self.b[1:])
        np.subtract(self.lb, self.b[1:], self.b[1:])
        self.b[0] = x
        
        self.lb[:] = self.b[:-1]
        
    def get_f(self):
        return self.f[-1]
    
    def get_b(self):
        return self.b[-1]
        
f = LatticeFilter(1)
f.rb[0] = 0.5
f.rf[0] = 0.5

f.input(1.0)

print f.get_f()
print f.get_b()

f.input(1.0)

print f.get_f()
print f.get_b()

f.input(1.0)

print f.get_f()
print f.get_b()
