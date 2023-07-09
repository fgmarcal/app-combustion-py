import numpy as np
import bagasse
import natural_gas
import firewood
import liquid_gas
import oil
import oxygen


x_data = []
y_data = []
combust = ""

def interpolate(x_axis, y_axis, value):
    grau = 10
    ajuste = np.polyfit(x_axis, y_axis, grau)
    p = np.poly1d(ajuste)
    return p(value)

# initial = int((input("Escolha a entrada incial: \n1.Excesso de ar \n2.CO2 \n3.Oxigênio ")))


# value = float(input("Insira um valor de excesso de ar: "))

# fuel = int(input("Selecione um combustível: \n1.Bagaco \n2.Gas Natural \n3.Lenha \n4.GLP \n5.Oleo Pesado\n"))

# match fuel:
#     case 1:
#         combust = "Bagaço"
#         x_data = bagasse.air_excess
#         y_data = bagasse.co2
#     case 2:
#         combust = "Gas Natural"
#         x_data = natural_gas.air_excess
#         y_data = natural_gas.co2
#     case 3:
#         combust = "Lenha"
#         x_data = firewood.air_excess
#         y_data = firewood.co2
#     case 4:
#         combust = "GLP"
#         x_data = liquid_gas.air_excess
#         y_data = liquid_gas.co2
#     case 5:
#         combust = "Óleo Pesado"
#         x_data = oil.air_excess
#         y_data = oil.co2
#     case _:
#         print("Não válido")


# co2 = interpolate(x_data, y_data, value)

# o2 = interpolate(oxygen.air_excess, oxygen.co2, co2)

# print(f"Para o valor de {value} de excesso de ar, o CO2 é {co2} e o Oxigênio é {o2} na queima de {combust}")

