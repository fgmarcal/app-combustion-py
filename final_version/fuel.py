import bagasse
import firewood
import liquid_gas
import natural_gas
import oil
import oxygen
from engine import interpolate

FUEL_LIST = ["Bagaço", "Lenha", "GLP", "Gás Natural", "Óleo Pesado"]
OPTION_LIST = ["Excesso de ar", "CO2", "O2"]

class Fuel:

    def __init__(self, fuel, option):
        self.fuel = fuel
        self.option = option

#TODO 1) add fuel logic 2) test

    
