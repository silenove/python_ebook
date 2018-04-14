# -*- coding: utf-8 -*-
from enthought.traits.api import \
    Str, Float, HasTraits, Property, cached_property, Range, Instance, on_trait_change, Enum

from enthought.chaco.api import Plot, AbstractPlotData, ArrayPlotData, VPlotContainer

from enthought.traits.ui.api import \
    Item, View, VGroup, HSplit, ScrubberEditor, VSplit

from enthought.enable.api import Component, ComponentEditor
from enthought.chaco.tools.api import PanTool, ZoomTool 

import numpy as np

# 鼠标拖动修改值的控件的样式
scrubber = ScrubberEditor(
    hover_color  = 0xFFFFFF, 
    active_color = 0xA0CD9E, 
    border_color = 0x808080
)

# 取FFT计算的结果freqs中的前n项进行合成，返回合成结果，计算loops个周期的波形
def fft_combine(freqs, n, loops=1):
    length = len(freqs) * loops
    data = np.zeros(length)
    index = loops * np.arange(0, length, 1.0) / length * (2 * np.pi)
    for k, p in enumerate(freqs[:n]):
        if k != 0: p *= 2 # 除去直流成分之外，其余的系数都*2
        data += np.real(p) * np.cos(k*index) # 余弦成分的系数为实数部
        data -= np.imag(p) * np.sin(k*index) # 正弦成分的系数为负的虚数部
    return index, data    

class TriangleWave(HasTraits):
    # 指定三角波的最窄和最宽范围，由于Range似乎不能将常数和traits名混用
    # 所以定义这两个不变的trait属性
    low = Float(0.02)
    hi = Float(1.0)

    # 三角波形的宽度
    wave_width = Range("low", "hi", 0.5)

    # 三角波的顶点C的x轴坐标
    length_c = Range("low", "wave_width", 0.5)

    # 三角波的定点的y轴坐标
    height_c = Float(1.0)

    # FFT计算所使用的取样点数，这里用一个Enum类型的属性以供用户从列表中选择
    fftsize = Enum( [(2**x) for x in range(6, 12)])

    # FFT频谱图的x轴上限值
    fft_graph_up_limit = Range(0, 400, 20)

    # 用于显示FFT的结果
    peak_list = Str

    # 采用多少个频率合成三角波
    N = Range(1, 40, 4)

    # 保存绘图数据的对象
    plot_data = Instance(AbstractPlotData)    

    # 绘制波形图的容器
    plot_wave = Instance(Component)

    # 绘制FFT频谱图的容器
    plot_fft  = Instance(Component)

    # 包括两个绘图的容器
    container = Instance(Component)

    # 设置用户界面的视图， 注意一定要指定窗口的大小，这样绘图容器才能正常初始化
    view = View(
        HSplit(
            VSplit(
                VGroup(
                    Item("wave_width", editor = scrubber, label=u"波形宽度"),
                    Item("length_c", editor = scrubber, label=u"最高点x坐标"),
                    Item("height_c", editor = scrubber, label=u"最高点y坐标"),
                    Item("fft_graph_up_limit", editor = scrubber, label=u"频谱图范围"),
                    Item("fftsize", label=u"FFT点数"),
                    Item("N", label=u"合成波频率数")
                ),
                Item("peak_list", style="custom", show_label=False, width=100, height=250)
            ),
            VGroup(
                Item("container", editor=ComponentEditor(size=(600,300)), show_label = False),
                orientation = "vertical"
            )
        ),
        resizable = True,
        width = 800,
        height = 600,
        title = u"三角波FFT演示"
    )

    # 创建绘图的辅助函数，创建波形图和频谱图有很多类似的地方，因此单独用一个函数以
    # 减少重复代码
    def _create_plot(self, data, name, type="line"):
        p = Plot(self.plot_data)
        p.plot(data, name=name, title=name, type=type)
        p.tools.append(PanTool(p))
        zoom = ZoomTool(component=p, tool_mode="box", always_on=False)
        p.overlays.append(zoom)        
        p.title = name
        return p

    def __init__(self):
        # 首先需要调用父类的初始化函数
        super(TriangleWave, self).__init__()

        # 创建绘图数据集，暂时没有数据因此都赋值为空，只是创建几个名字，以供Plot引用
        self.plot_data = ArrayPlotData(x=[], y=[], f=[], p=[], x2=[], y2=[]) 

        # 创建一个垂直排列的绘图容器，它将频谱图和波形图上下排列
        self.container = VPlotContainer()

        # 创建波形图，波形图绘制两条曲线： 原始波形(x,y)和合成波形(x2,y2)
        self.plot_wave = self._create_plot(("x","y"), "Triangle Wave")
        self.plot_wave.plot(("x2","y2"), color="red")

        # 创建频谱图，使用数据集中的f和p
        self.plot_fft  = self._create_plot(("f","p"), "FFT", type="scatter")

        # 将两个绘图容器添加到垂直容器中
        self.container.add( self.plot_wave )
        self.container.add( self.plot_fft )

        # 设置
        self.plot_wave.x_axis.title = "Samples"
        self.plot_fft.x_axis.title = "Frequency pins"
        self.plot_fft.y_axis.title = "(dB)"

        # 改变fftsize为1024，因为Enum的默认缺省值为枚举列表中的第一个值
        self.fftsize = 1024

    # FFT频谱图的x轴上限值的改变事件处理函数，将最新的值赋值给频谱图的响应属性
    def _fft_graph_up_limit_changed(self):
        self.plot_fft.x_axis.mapper.range.high = self.fft_graph_up_limit

    def _N_changed(self):
        self.plot_sin_combine()

    # 多个trait属性的改变事件处理函数相同时，可以用@on_trait_change指定
    @on_trait_change("wave_width, length_c, height_c, fftsize")        
    def update_plot(self):
        # 计算三角波
        global y_data
        x_data = np.arange(0, 1.0, 1.0/self.fftsize)
        func = self.triangle_func()
        # 将func函数的返回值强制转换成float64
        y_data = np.cast["float64"](func(x_data))

        # 计算频谱
        fft_parameters = np.fft.fft(y_data) / len(y_data)

        # 计算各个频率的振幅
        fft_data = np.clip(20*np.log10(np.abs(fft_parameters))[:self.fftsize/2+1], -120, 120)

        # 将计算的结果写进数据集
        self.plot_data.set_data("x", np.arange(0, self.fftsize)) # x坐标为取样点
        self.plot_data.set_data("y", y_data)
        self.plot_data.set_data("f", np.arange(0, len(fft_data))) # x坐标为频率编号
        self.plot_data.set_data("p", fft_data)

        # 合成波的x坐标为取样点，显示2个周期
        self.plot_data.set_data("x2", np.arange(0, 2*self.fftsize)) 

        # 更新频谱图x轴上限
        self._fft_graph_up_limit_changed()

        # 将振幅大于-80dB的频率输出
        peak_index = (fft_data > -80)
        peak_value = fft_data[peak_index][:20]
        result = []
        for f, v in zip(np.flatnonzero(peak_index), peak_value):
            result.append("%s : %s" %(f, v) )
        self.peak_list = "\n".join(result)

        # 保存现在的fft计算结果，并计算正弦合成波
        self.fft_parameters = fft_parameters
        self.plot_sin_combine()

    # 计算正弦合成波，计算2个周期
    def plot_sin_combine(self):
        index, data = fft_combine(self.fft_parameters, self.N, 2)
        self.plot_data.set_data("y2", data)               

    # 返回一个ufunc计算指定参数的三角波
    def triangle_func(self):
        c = self.wave_width
        c0 = self.length_c
        hc = self.height_c

        def trifunc(x):
            x = x - int(x) # 三角波的周期为1，因此只取x坐标的小数部分进行计算
            if x >= c: r = 0.0
            elif x < c0: r = x / c0 * hc
            else: r = (c-x) / (c-c0) * hc
            return r

        # 用trifunc函数创建一个ufunc函数，可以直接对数组进行计算, 不过通过此函数
        # 计算得到的是一个Object数组，需要进行类型转换
        return np.frompyfunc(trifunc, 1, 1)    

if __name__ == "__main__":
    triangle = TriangleWave()
    triangle.configure_traits()
