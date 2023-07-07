import numpy as np
import matplotlib.pyplot as plt

x_data = []
y_data = []

grau = 10

ajuste = np.polyfit(x_data, y_data, grau)
p = np.poly1d(ajuste)

x_interpolados = np.linspace(min(x_data), max(x_data), 100)
y_interpolados = p(x_interpolados)

def return_x(x):
    return p(x)