import bagasse
import firewood
import liquid_gas
import natural_gas
import oil
import oxygen
from engine import interpolate

FUEL_LIST = {
    "Bagaço":{"Excesso de Ar" : bagasse.air_excess, "CO2" : bagasse.co2}, 
    "Lenha" :{"Excesso de Ar" : firewood.air_excess, "CO2" : firewood.co2}, 
    "GLP" : {"Excesso de Ar" : liquid_gas.air_excess, "CO2" : liquid_gas.co2}, 
    "Gás Natural" : {"Excesso de Ar" : natural_gas.air_excess, "CO2" : natural_gas.co2}, 
    "Óleo Pesado" : {"Excesso de Ar" : oil.air_excess, "CO2" : oil.co2},
    }

OPTION_LIST = ["Excesso de Ar", "CO2", "O2"]

class Fuel:

    def __init__(self, fuel, option):
        self.fuel = fuel
        self.option = option

#TODO 1) add fuel logic 2) test
    def return_result_txt(self,fuel, excess, co2, o2):
        """returns text for popup"""
        return f"Combustível: {str(fuel)}\n\nExcesso de ar: {float(excess):.4f}\n\nCO2: {float(co2):.4f}\n\nO2: {float(o2):.4f}"

    def return_options(self, value):
        """returns the option based on fuel selection"""
        if self.option == OPTION_LIST[0]:
            return_co2 = interpolate(x_axis=FUEL_LIST[self.fuel].get(str(OPTION_LIST[0])), y_axis=FUEL_LIST[self.fuel].get(str(OPTION_LIST[1])), value=value)
            return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=value)
            result = self.return_result_txt(self.fuel, value, return_co2, return_o2)
            return result
        elif self.option == OPTION_LIST[1]:
            return_excess = interpolate(x_axis=FUEL_LIST[self.fuel].get(str(OPTION_LIST[1])), y_axis=FUEL_LIST[self.fuel].get(str(OPTION_LIST[0])), value=value)
            return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
            result = self.return_result_txt(self.fuel, return_excess, value, return_o2)
            return result
        elif self.option == OPTION_LIST[2]:
            return_excess = interpolate(x_axis=oxygen.o2,y_axis=oxygen.air_excess, value=value)
            return_co2 = interpolate(x_axis=FUEL_LIST[self.fuel].get(str(OPTION_LIST[0])), y_axis=FUEL_LIST[self.fuel].get(str(OPTION_LIST[1])), value=return_excess)
            result = self.return_result_txt(self.fuel, return_excess, return_co2, value)
            return result
