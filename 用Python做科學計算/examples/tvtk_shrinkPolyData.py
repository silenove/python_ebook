# -*- coding: utf-8 -*-
from enthought.tvtk.api import tvtk
from enthought.tvtk.tools import ivtk
from enthought.pyface.api import GUI

part =tvtk.STLReader(file_name = "42400-IDGH.stl")
shrink = tvtk.ShrinkPolyData(input = part.output, shrink_factor = 0.50 )
part_mapper = tvtk.PolyDataMapper( input = shrink.output )
part_actor = tvtk.Actor( mapper = part_mapper )

gui = GUI()
window = ivtk.IVTKWithBrowser(size=(800,600))
window.open()
window.scene.add_actor( part_actor ) 
gui.start_event_loop()
