import numpy as np

def error():
    raise ValueError("Value not found")

def interpolate(x_axis, y_axis, value):
    if value >= x_axis[0] and value <= x_axis[-1]:
        grau = 10
        ajuste = np.polyfit(x_axis, y_axis, grau)
        p = np.poly1d(ajuste)
        return p(value)
    else:
        error() 

#TODO