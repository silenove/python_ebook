# -*- coding: utf-8 -*-
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as pl

# 产生1024点4个周期的正弦波
t = np.linspace(0, 8*np.pi, 1024, endpoint=False)
x = np.sin(t)

# 进行Hilbert变换
y = fftpack.hilbert(x)
pl.plot(x, label=u"原始波形")
pl.plot(y, label=u"Hilbert转换后的波形")
pl.legend()
pl.show()
