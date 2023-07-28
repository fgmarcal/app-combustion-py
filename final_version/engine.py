import numpy as np

def interpolate(x_axis, y_axis, value):
    try:
        return np.interp(value, x_axis, y_axis)
    except Exception as err:
        print(err)
        return 0
