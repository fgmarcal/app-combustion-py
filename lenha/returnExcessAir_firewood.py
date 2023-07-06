import numpy as np
import matplotlib.pyplot as plt

# Pares ordenados fornecidos
y_data = np.array([0.465822078, 4.037990075, 7.599723948, 10.91875144, 14.98930297, 19.05802853, 23.6347481, 28.71247987, 33.28659133, 38.1063377, 43.67957003, 49.53681977, 54.83193216, 60.40484556, 65.97561537, 71.5413765, 77.10774411, 82.62530481, 88.23725872, 93.80159776, 99.36044712, 104.9189044, 110.4814135, 116.0388774, 121.5966288, 127.1539097, 132.7096221, 138.2632955, 143.8204195, 147.605475])
x_data = np.array([19.77479641, 19.09712215, 18.57477724, 17.91552134, 17.31857756, 16.74881643, 16.11671766, 15.52621739, 14.93294485, 14.43298712, 13.96613527, 13.43787738, 12.94463768, 12.48253355, 12.05234031, 11.69670961, 11.33205046, 10.9439635, 10.65067633, 10.31621578, 10.06347826, 9.8165781, 9.509358561, 9.277246377, 9.040853462, 8.811465378, 8.605426731, 8.429742351, 8.202689211, 8.105829308])

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
def returnExcessFromCO2_firewood(x):
    return p(x)

# Exemplo de uso
x = eval(input('informe o valor do co2: '))
resultado = returnExcessFromCO2_firewood(x)
print(resultado)