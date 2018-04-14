# -*- coding: utf-8 -*-
from enthought.tvtk.api import tvtk

# 创建一个圆锥数据源，并且同时设置其高度，底面半径和底面圆的分辨率(用36边形近似)
cs = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36)
# 使用PolyDataMapper将数据转换为图形数据
m = tvtk.PolyDataMapper(input = cs.output)
# 创建一个Actor
a = tvtk.Actor(mapper=m)
# 创建一个Renderer，将Actor添加进去
ren = tvtk.Renderer(background=(0.1, 0.2, 0.4))
ren.add_actor(a)
# 创建一个RenderWindow(窗口)，将Renderer添加进去
rw = tvtk.RenderWindow(size=(300,300))
rw.add_renderer(ren)
# 创建一个RenderWindowInteractor（窗口的交互工具)
rwi = tvtk.RenderWindowInteractor(render_window=rw)
# 开启交互
rwi.initialize()
rwi.start()
