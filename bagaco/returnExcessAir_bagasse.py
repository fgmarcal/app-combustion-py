import numpy as np
import matplotlib.pyplot as plt

# Pares ordenados fornecidos
y_data = np.array([0.496138552, 3.556130665, 7.125094482, 10.43683383, 14.50980561, 20.61030596, 25.79782444, 30.76869105, 37.10936487, 42.68484012, 48.26407972, 53.83437899, 59.30492294, 64.46825397, 70.74574419, 76.16292846, 81.67646444, 87.23907815, 93.03048079, 97.52495974, 104.9368635, 110.4957128, 115.9901369, 121.610902, 127.1689671, 132.7248364, 138.2810193, 143.8346927, 148.5472165])
x_data = np.array([19.32348516, 18.77040258, 18.14042788, 17.5896681, 16.95669485, 16.14057971, 15.52286404, 14.91608696, 14.27458937, 13.77434783, 13.21806763, 12.79487923, 12.35671498, 11.991927, 11.54102254, 11.14720612, 10.81903382, 10.51025765, 10.12891036, 9.887767042, 9.549227053, 9.296489533, 9.065330113, 8.828373591, 8.587310789, 8.378937198, 8.16589372, 7.99020934, 7.83643854])

# Grau do polinômio de ajuste
grau = 10

# Ajuste polinomial
ajuste = np.polyfit(x_data, y_data, grau)
p = np.poly1d(ajuste)

# Valores interpolados
x_interpolados = np.linspace(min(x_data), max(x_data), 100)
y_interpolados = p(x_interpolados)

# # Gráfico dos pontos e do polinômio ajustado
# plt.plot(x_data, y_data, 'bo', label='Pares Ordenados')
# plt.plot(x_interpolados, y_interpolados, 'r-', label='Ajuste Polinomial')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

# Função para retornar o valor interpolado
def returnExcessFromCO2_bagasse(x):
    return p(x)

# Exemplo de uso
x = eval(input('informe o valor do CO2: '))
resultado = returnExcessFromCO2_bagasse(x)
print(resultado)