import numpy as np


def interpolate(x_axis, y_axis, value):
    grau = 10
    ajuste = np.polyfit(x_axis, y_axis, grau)
    p = np.poly1d(ajuste)
    return p(value)