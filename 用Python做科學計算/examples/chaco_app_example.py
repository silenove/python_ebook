from enthought.traits.api import HasTraits, Instance, Int, Color
from enthought.traits.ui.api import View, Group, Item
from enthought.enable.component_editor import ComponentEditor
from enthought.chaco.api import marker_trait, Plot, ArrayPlotData
from numpy import linspace, sin

class ScatterPlotTraits(HasTraits):

    plot = Instance(Plot)
    color = Color("blue")
    marker = marker_trait
    marker_size = Int(4)

    traits_view = View(
        Group(Item('color', label="Color"),
              Item('marker', label="Marker"),
              Item('marker_size', label="Size"),
              Item('plot', editor=ComponentEditor(), show_label=False),
                   orientation = "vertical"),
              width=800, height=600, resizable=True, title="Chaco Plot")

    def __init__(self):
        super(ScatterPlotTraits, self).__init__()
        x = linspace(-14, 14, 100)
        y = sin(x) * x**3
        plotdata = ArrayPlotData(x = x, y = y)
        plot = Plot(plotdata)

        self.renderer = plot.plot(("x", "y"), type="scatter", color="blue")[0]
        self.plot = plot

    def _color_changed(self):
        self.renderer.color = self.color

    def _marker_changed(self):
        self.renderer.marker = self.marker

    def _marker_size_changed(self):
        self.renderer.marker_size = self.marker_size

if __name__ == "__main__":
    ScatterPlotTraits().configure_traits()
