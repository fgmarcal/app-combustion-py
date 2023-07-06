import numpy as np
import matplotlib.pyplot as plt

# Pares ordenados fornecidos
y_data = np.array([1.765486871, 5.247198396, 8.482516678, 11.46992179, 14.95946917, 18.95166207, 23.19662347, 27.69020781, 32.44070623, 36.93760064, 41.88019036, 47.192808, 52.70240709, 58.20996717, 63.72301692, 69.23763515, 74.75214882, 80.01696572, 85.78792061, 91.30740113, 96.83237133, 102.3501265, 107.8742811, 113.3991781, 118.9240438, 124.4493799, 129.9759709, 135.5036075, 141.0324466, 146.310789, 149.626409])
x_data = np.array([0.427119853, 1.096040948, 1.682936125, 2.210432099, 2.762703301, 3.332258454, 3.888933023, 4.494440866, 5.025354267, 5.581586151, 6.065400564, 6.665732689, 7.146167472, 7.656956522, 8.086022544, 8.49173913, 8.899012346, 9.273438003, 9.6131562, 9.946489533, 10.19809984, 10.55711755, 10.82086957, 11.07356951, 11.32673645, 11.57289855, 11.80038111, 12.01229737, 12.2063124, 12.37938808, 12.52085883])

# Grau do polinômio de ajuste
grau = 10

# Ajuste polinomial
ajuste = np.polyfit(x_data, y_data, grau)
p = np.poly1d(ajuste)

# Valores interpolados
x_interpolados = np.linspace(min(x_data), max(x_data), 100)
y_interpolados = p(x_interpolados)

# Gráfico dos pontos e do polinômio ajustado
plt.plot(x_data, y_data, 'bo', label='Pares Ordenados')
plt.plot(x_interpolados, y_interpolados, 'r-', label='Ajuste Polinomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Função para retornar o valor interpolado
def returnExcessAirFromO2(x):
    return p(x)
# Exemplo de uso
x = eval(input('informe o valor do O2: '))
resultado = returnExcessAirFromO2(x)
print(resultado)