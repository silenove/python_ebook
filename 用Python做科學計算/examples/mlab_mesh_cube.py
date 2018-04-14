# -*- coding: utf-8 -*-
from numpy import *
from enthought.mayavi import mlab

x = [[-1,1,1,-1,-1],
[-1,1,1,-1,-1]]

y = [[-1,-1,-1,-1,-1],
[1,1,1,1, 1]]

z = [[1,1,-1,-1,1],
[1,1,-1,-1,1]]

#box = mlab.mesh(x, y, z, representation="surface")
#mlab.axes(xlabel='x', ylabel='y', zlabel='z')
#mlab.outline(box)
#mlab.show()

print [(a,b,c) for a,b,c in zip(x[1],y[1],z[1])]