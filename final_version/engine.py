import numpy as np

def error():
    raise ValueError("Value not found")

def interpolate(x_axis, y_axis, value):
    if value >= x_axis[0] and value <= x_axis[-1]:
        degree = 10
        adjust = np.polyfit(x_axis, y_axis, degree)
        point = np.poly1d(adjust)
        return point(value)
    else:
        error() 

#TODO