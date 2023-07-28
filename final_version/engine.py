import numpy as np

def interpolate(x_axis, y_axis, value):
    try:
        grau = 10
        ajuste = np.polyfit(x_axis, y_axis, grau)
        p = np.poly1d(ajuste)
        result = p(value)
        if result < 0 or result > 150:
            return 0
        else:
            return result

    except Exception as err:
        print(err)
        return 0