# -*- coding: utf-8 -*-
from enthought.tvtk.api import tvtk

# 载入ivtk所需要的对象
from enthought.tvtk.tools import ivtk
from enthought.pyface.api import GUI

cs = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36)
m = tvtk.PolyDataMapper(input = cs.output)
a = tvtk.Actor(mapper=m)

# 创建一个GUI对象，和一个带Crust(Python shell)的ivtk窗口
gui = GUI()
window = ivtk.IVTKWithCrustAndBrowser(size=(800,600))
window.open()
window.scene.add_actor( a ) # 将圆锥的actor添加进窗口的场景中
gui.start_event_loop()
#window.scene.reset_zoom()
