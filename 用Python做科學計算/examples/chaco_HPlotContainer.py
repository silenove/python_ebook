from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import HPlotContainer, ArrayPlotData, Plot
from enthought.enable.component_editor import ComponentEditor
from numpy import linspace, sin

class ContainerExample(HasTraits):
    plot = Instance(HPlotContainer)
    traits_view = View(Item('plot', editor=ComponentEditor(), show_label=False),
                       width=1000, height=600, resizable=True, title="Chaco Plot")
    def __init__(self):
        super(ContainerExample, self).__init__()
        x = linspace(-14, 14, 100)
        y = sin(x) * x**3
        plotdata = ArrayPlotData(x=x, y=y)
        scatter = Plot(plotdata)
        scatter.plot(("x", "y"), type="scatter", color="blue")
        line = Plot(plotdata)
        line.plot(("x", "y"), type="line", color="blue")
        container = HPlotContainer(scatter, line)
        self.plot = container

if __name__ == "__main__":
    ContainerExample().configure_traits()
