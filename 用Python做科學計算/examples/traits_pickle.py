# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 12:26:40 2009

@author: w-son
"""

#from enthought.sweet_pickle import dumps, loads
from pickle import dumps, loads
from enthought.traits.api import HasTraits, List, Float

class C(HasTraits):
    #a = List([1])
    a = Float(0)
    pass

loads(dumps(C()))