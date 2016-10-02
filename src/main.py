#!usr/bin/env python3.5
# main.py

from collections import deque
from datetime import datetime
from math import pi, sin
from random import random

from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure, curdoc

# create a plot and style its properties
p = figure()
r = p.line(x=[], y=[], line_width=2)

p.xaxis.formatter = DatetimeTickFormatter(formats={
        'seconds': ['%H:%M:%S'],
        'minutes': ['%H:%M:%S'],
        'hours': ['%H:%M:%S'],
    }
)

ds = r.data_source
data = {
        'x': deque(maxlen=20),
        'y': deque(maxlen=20),
       }


def add_value():
    time = datetime.now()
    data['x'].append(time)
    data['y'].append(random() + sin(pi*time.second/5))
    ds.data = {key: list(item) for key, item in data.items()}


curdoc().add_root(column(p))
curdoc().add_periodic_callback(add_value, 1000)
