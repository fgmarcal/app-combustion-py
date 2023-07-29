import numpy as np
GRAPHIC_MAX = 150
GRAPHIC_MIN = 0
def interpolate(x_axis, y_axis, value):
    try:
        grau = 10
        ajuste = np.polyfit(x_axis, y_axis, grau)
        p = np.poly1d(ajuste)
        result = p(value)
        if result < GRAPHIC_MIN or result > GRAPHIC_MAX:
            return 0
        else:
            return result

    except Exception as err:
        print(err)
        return 0
