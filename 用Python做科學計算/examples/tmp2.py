# -*- coding: utf-8 -*-
"""
Created on Sat Jan 02 19:53:11 2010

@author: HY
"""
import numpy as np
triangle = np.array([[0,0],[1,0],[3,2]],dtype=np.float)

A = triangle[0]
B = triangle[1]
C = triangle[2]
AB = A-B
AC = A-C

print np.abs(np.cross(AB,AC)/2.0)