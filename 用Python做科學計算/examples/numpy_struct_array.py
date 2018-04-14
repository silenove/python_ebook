# -*- coding: utf-8 -*-
import numpy as np
persontype = np.dtype({
    'names':['name', 'age', 'weight'],
    'formats':['S30','i', 'f']}, align= True )
a = np.array([("Zhang",32,75.5),("Wang",24,65.2)],
    dtype=persontype)
c = a[1]
c["name"] = "Li"
a.tofile("test.bin")