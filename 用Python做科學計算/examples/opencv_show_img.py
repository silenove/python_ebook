# -*- coding: utf-8 -*-
from opencv.highgui import *
import sys

img = cvLoadImage( sys.argv[1] )
cvNamedWindow("Example1", CV_WINDOW_AUTOSIZE)
cvShowImage("Example1", img)
cvWaitKey(0)