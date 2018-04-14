from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData, Legend
from enthought.enable.component_editor import ComponentEditor
from numpy import linspace, sin, cos

class LinePlot(HasTraits):
    plot = Instance(Plot)
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")

    def __init__(self):
        super(LinePlot, self).__init__()
        x = linspace(-14, 14, 100)
        y1 = sin(x) * x**3
        y2 = cos(x) * x**3
        plotdata = ArrayPlotData(x=x, y1=y1, y2=y2)
        plot = Plot(plotdata)
        plot.plot(("x", "y1"), type="line", color="blue", name="sin(x) * x**3")
        plot.plot(("x", "y2"), type="line", color="red", name="cos(x) * x**3")
        plot.plot(("x", "y2"), type="scatter", color="red", marker = "circle",
                  marker_size = 2, name="cos(x) * x**3 points")
        plot.title = "Multiple Curves"
        self.plot = plot

        legend = Legend(padding=10, align="ur")
        legend.plots = plot.plots
        plot.overlays.append(legend)        

if __name__ == "__main__":
    lineplot = LinePlot()
    lineplot.configure_traits()
