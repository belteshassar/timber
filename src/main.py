#!usr/bin/env python3.5

from collections import deque
from datetime import datetime
from math import pi, sin
from random import random
from statistics import mean

from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure, curdoc

fig = figure()
value = fig.line(x=[], y=[], line_width=2)
rolling_avg = fig.line(x=[], y=[], line_width=2)

fig.xaxis.formatter = DatetimeTickFormatter(formats={
        'seconds': ['%H:%M:%S'],
        'minutes': ['%H:%M:%S'],
        'hours': ['%H:%M:%S'],
    }
)

data = {
        'x': deque(maxlen=100),
        'y': deque(maxlen=100),
       }

y_avg = deque(maxlen=100)


def add_value():
    time = datetime.now()
    data['x'].append(time)
    data['y'].append(random() + sin(pi*time.second/5))
    y_avg.append(mean(data['y']))
    value.data_source.data = {key: list(item) for key, item in data.items()}

    rolling_avg.data_source.data = {
        'x': list(data['x']),
        'y': list(y_avg),
    }


curdoc().add_root(column(fig))
curdoc().add_periodic_callback(add_value, 2000)
