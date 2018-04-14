# -*- coding: utf-8 -*-
from scipy import fftpack
import numpy as np

x = np.random.rand(16)
y = fftpack.hilbert(x)

X = np.fft.fft(x)
Y = np.fft.fft(y)

np.imag(Y/X)