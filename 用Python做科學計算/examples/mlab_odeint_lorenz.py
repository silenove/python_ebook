# -*- coding: utf-8 -*-
from scipy.integrate import odeint 
import numpy as np 

def lorenz(w, t, p, r, b): 
    x, y, z = w
    return np.array([p*(y-x), x*(r-z)-y, x*y-b*z]) 

t = np.arange(0, 30, 0.01) 
track1 = odeint(lorenz, (0.0, 1.00, 0.0), t, args=(10.0, 28.0, 3.0)) 

from enthought.mayavi import mlab
mlab.plot3d(track1[:,0], track1[:,1], track1[:,2],color=(1,0,0), tube_radius=0.1)
mlab.show()