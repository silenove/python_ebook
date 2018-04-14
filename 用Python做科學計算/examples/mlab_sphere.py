# -*- coding: utf-8 -*-
import numpy as np
from enthought.mayavi import mlab
from enthought.mayavi.modules.scalar_cut_plane import ScalarCutPlane

def sphere(x, y, z):
    return x**2+y**2+z**2

x, y, z = np.mgrid[-1:1:20j, -1:1:20j, 0:1:10j]
surface = mlab.contour3d(sphere(x,y,z), transparent=True)
surface.contour.auto_contours = False
surface.contour.contours = [1.0]
surface.actor.property.opacity = 0.3

axes =mlab.axes(xlabel='x', ylabel='y', zlabel='z')
axes.axes.use_ranges = True
axes.axes.ranges = np.array([-1., -1.,  0.,  1.,  1.,  1.])

engine = mlab.get_engine()
module_manager = engine.scenes[0].children[0].children[0]

cut_plane = ScalarCutPlane()
engine.add_filter(cut_plane, module_manager)

cut_plane.warp_scalar.filter.normal = np.array([ 1.,  0.,  0.])
cut_plane.enable_contours = True
cut_plane.contour.auto_contours = True
cut_plane.contour.maximum_contour = 1.0
cut_plane.contour.number_of_contours = 3
cut_plane.contour.filled_contours = True
cut_plane.implicit_plane.widget.origin = np.array([ 15,10,5])
cut_plane.implicit_plane.widget.enabled = False

circle = ScalarCutPlane()
engine.add_filter(circle, module_manager)

circle.enable_contours = True
circle.contour.auto_contours = False
circle.contour.contours[0:1] = [1.0]
circle.implicit_plane.widget.origin = np.array([ 15,10,1.1])
circle.implicit_plane.widget.normal = np.array([ 0.,  0.,  1.])
circle.implicit_plane.widget.enabled = False

mlab.show()