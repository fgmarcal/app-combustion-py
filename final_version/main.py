from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
from engine import interpolate
import bagasse
import firewood
import liquid_gas
import natural_gas
import oil
import oxygen
import locale

locale.setlocale(locale.LC_ALL, '')
class CombustApp(App):

    def build(self):
        super().build()
        layout = BoxLayout(orientation='vertical', size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        Window.clearcolor = (get_color_from_hex('#D49B54'))

        header_label = Label(text='COMBUSTÃO', font_name='Anton', font_size='50sp', color="#46244C")
        layout.add_widget(header_label)

        menu_button = Button(text='Selecione o Combustível', font_name='Anton', font_size='20sp', size_hint=(1, 0.8) , background_color="#712B75")
        menu_button.bind(on_release=self.show_menu)
        layout.add_widget(menu_button)

        self.dropdown = DropDown()
        fuels = ["Bagaço", "Lenha", "GLP", "Gás Natural", "Óleo Pesado"]
        for fuel in fuels:
            btn = Button(text=fuel, size_hint_y=None, height=50, font_name='Anton', font_size='18sp', background_color="#C74B50")
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            btn.bind(on_release=lambda btn: self.on_dropdown_select(value=btn.text))
            self.dropdown.add_widget(btn)

        self.selected_fuel_label = Label(text='', font_name='Anton', font_size='30sp', color="#890F0D")
        layout.add_widget(self.selected_fuel_label)

        self.blank_space_1 = Label(text='')
        layout.add_widget(self.blank_space_1)

        self.input_text = TextInput(hint_text='Insira um valor:', font_name='Anton', font_size='19sp',
                                    multiline=False, input_type='number', size_hint=(0.5, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.input_text)


        layout.add_widget(Label(text="Selecione o tipo de entrada:", font_name='Anton', font_size='30sp', color="#C74B50"))
        toggle_button = ToggleButton(text='Excesso de ar', font_name='Anton', font_size='20sp', group='options', size_hint_y=0.5, background_color="#C2DEDC")
        toggle_button.bind(on_press=self.on_toggle_button)
        layout.add_widget(toggle_button)

        toggle_button = ToggleButton(text='CO2', font_name='Anton', font_size='20sp', group='options', size_hint_y=0.5, background_color="#C2DEDC")
        toggle_button.bind(on_press=self.on_toggle_button)
        layout.add_widget(toggle_button)

        toggle_button = ToggleButton(text='O2', font_name='Anton', font_size='20sp', group='options', size_hint_y=0.5, background_color="#C2DEDC")
        toggle_button.bind(on_press=self.on_toggle_button)
        layout.add_widget(toggle_button)

        self.blank_space_2 = Label(text='')
        layout.add_widget(self.blank_space_2)

        calculate_button = Button(text='Calcular', font_name='Anton', font_size='20sp', size_hint=(0.4, 0.8),pos_hint={'center_x': 0.5, 'center_y': 0.5},background_color="#46244C")
        calculate_button.bind(on_release=self.calculate)
        layout.add_widget(calculate_button)


        return layout


    def show_menu(self, button):
        self.dropdown.open(button)

    def on_toggle_button(self, button):
        self.selected_option = button.text

    def calculate(self, button):
        try:
            input_value = locale.atof(self.input_text.text)
            fuel = self.selected_fuel_label.text
            option = self.selected_option
            result = ''
            popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
            #fuel selection - bagasse
            if fuel == "Bagaço" and option == "Excesso de ar":
                return_co2 = interpolate(bagasse.air_excess, bagasse.co2, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=input_value)
                result = f"Combustível: {fuel}\n\nExcesso de ar: {input_value}\n\nCO2: {return_co2}\n\nO2: {return_o2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            elif fuel == "Bagaço" and option == "CO2":
                return_excess = interpolate(bagasse.co2, bagasse.air_excess, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
                result = f"Combustível: {fuel}\n\nCO2: {input_value}\n\nExcesso de ar: {return_excess}\n\nO2: {return_o2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            elif fuel == "Bagaço" and option == "O2":
                return_excess = interpolate(oxygen.o2, oxygen.air_excess, input_value)
                return_Co2 = interpolate(x_axis=bagasse.air_excess,y_axis=bagasse.co2, value=return_excess)
                result = f"Combustível: {fuel}\n\nO2: {input_value}\n\nExcesso de ar: {return_excess}\n\nCO2: {return_Co2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            #change fuel - firewood
            elif fuel == "Lenha" and option == "Excesso de ar":
                return_co2 = interpolate(firewood.air_excess, firewood.co2, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=input_value)
                result = f"Combustível: {fuel}\n\nExcesso de ar: {input_value}\n\nCO2: {return_co2}\n\nO2: {return_o2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            elif fuel == "Lenha" and option == "CO2":
                return_excess = interpolate(firewood.co2, firewood.air_excess, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
                result = f"Combustível: {fuel}\n\nCO2: {input_value}\n\nExcesso de ar: {return_excess}\n\nO2: {return_o2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            elif fuel == "Lenha" and option == "O2":
                return_excess = interpolate(oxygen.o2, oxygen.air_excess, input_value)
                return_Co2 = interpolate(x_axis=firewood.air_excess,y_axis=firewood.co2, value=return_excess)
                result = f"Combustível: {fuel}\n\nO2: {input_value}\n\nExcesso de ar: {return_excess}\n\nCO2: {return_Co2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            #change fuel-liquid gas
            elif fuel == "GLP" and option == "Excesso de ar":
                return_co2 = interpolate(liquid_gas.air_excess, liquid_gas.co2, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=input_value)
                result = f"Combustível: {fuel}\n\nExcesso de ar: {input_value}\n\nCO2: {return_co2}\n\nO2: {return_o2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            elif fuel == "GLP" and option == "CO2":
                return_excess = interpolate(liquid_gas.co2, liquid_gas.air_excess, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
                result = f"Combustível: {fuel}\n\nCO2: {input_value}\n\nExcesso de ar: {return_excess}\n\nO2: {return_o2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            elif fuel == "GLP" and option == "O2":
                return_excess = interpolate(oxygen.o2, oxygen.air_excess, input_value)
                return_Co2 = interpolate(x_axis=liquid_gas.air_excess,y_axis=liquid_gas.co2, value=return_excess)
                result = f"Combustível: {fuel}\n\nO2: {input_value}\n\nExcesso de ar: {return_excess}\n\nCO2: {return_Co2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            #change fuel- natural gas
            elif fuel == "Gás Natural" and option == "Excesso de ar":
                return_co2 = interpolate(natural_gas.air_excess, natural_gas.co2, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=input_value)
                result = f"Combustível: {fuel}\n\nExcesso de ar: {input_value}\n\nCO2: {return_co2}\n\nO2: {return_o2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            elif fuel == "Gás Natural" and option == "CO2":
                return_excess = interpolate(natural_gas.co2, natural_gas.air_excess, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
                result = f"Combustível: {fuel}\n\nCO2: {input_value}\n\nExcesso de ar: {return_excess}\n\nO2: {return_o2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            elif fuel == "Gás Natural" and option == "O2":
                return_excess = interpolate(oxygen.o2, oxygen.air_excess, input_value)
                return_Co2 = interpolate(x_axis=natural_gas.air_excess,y_axis=natural_gas.co2, value=return_excess)
                result = f"Combustível: {fuel}\n\nO2: {input_value}\n\nExcesso de ar: {return_excess}\n\nCO2: {return_Co2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            #change fuel- oil
            elif fuel == "Óleo Pesado" and option == "Excesso de ar":
                return_co2 = interpolate(oil.air_excess, oil.co2, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=input_value)
                result = f"Combustível: {fuel}\n\nExcesso de ar: {input_value}\n\nCO2: {return_co2}\n\nO2: {return_o2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            elif fuel == "Óleo Pesado" and option == "CO2":
                return_excess = interpolate(oil.co2, oil.air_excess, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
                result = f"Combustível: {fuel}\n\nCO2: {input_value}\n\nExcesso de ar: {return_excess}\n\nO2: {return_o2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
            elif fuel == "Óleo Pesado" and option == "O2":
                return_excess = interpolate(oxygen.o2, oxygen.air_excess, input_value)
                return_Co2 = interpolate(x_axis=oil.air_excess,y_axis=oil.co2, value=return_excess)
                result = f"Combustível: {fuel}\n\nO2: {input_value}\n\nExcesso de ar: {return_excess}\n\nCO2: {return_Co2}"
                popup = Popup(title="Resultado", content=Label(text=result), size_hint=(None, None), size=(400, 400))
                popup.open()
        except:
            popup = Popup(title="Erro ao inserir valores", content=Label(text="ERRO\n\nVerifique se o valor inserido está correto"), size_hint=(None, None), size=(400, 400))
            popup.open()

    def on_start(self):
        self.selected_option = 'Excesso de ar'
    
    def clear_selection(self):
        pass

    def on_dropdown_select(self, value):
        self.selected_fuel_label.text = value
    
LabelBase.register(name='Anton',
                fn_regular='Anton-Regular.ttf')

if __name__ == '__main__':
    CombustApp().run()