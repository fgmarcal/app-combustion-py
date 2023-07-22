import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image
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

kivy.require('2.0.0')

__version__ = '1.0.9'
locale.setlocale(locale.LC_ALL, '')
class CombustApp(App):

    def build(self):
        super().build()
        layout = BoxLayout(orientation='vertical', size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        Window.clearcolor = (0.565, 0.56, 1)

        header_image = Image(source="flame.png", fit_mode="contain")
        layout.add_widget(header_image)

        menu_button = Button(text='Selecione o Combustível', font_name='Anton', font_size='20sp', size_hint=(1, 0.8) , background_color="#712B75")
        menu_button.bind(on_release=self.show_menu)
        layout.add_widget(menu_button)

        self.dropdown = DropDown()
        fuels = ["Bagaço", "Lenha", "GLP", "Gás Natural", "Óleo Pesado"]
        for fuel in fuels:
            btn = Button(text=fuel, size_hint_y=None, height=70, font_name='Anton', font_size='18sp', background_color="#C74B50")
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            btn.bind(on_release=lambda btn: self.on_dropdown_select(value=btn.text))
            self.dropdown.add_widget(btn)

        self.selected_fuel_label = Label(text='', font_name='Anton', font_size='30sp', color="#890F0D")
        layout.add_widget(self.selected_fuel_label)

        layout.add_widget(Label(text=''))

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

        layout.add_widget(Label(text=''))

        calculate_button = Button(text='Calcular', font_name='Anton', font_size='20sp', size_hint=(0.4, 0.8),pos_hint={'center_x': 0.5, 'center_y': 0.5},background_color="#C74B50")
        calculate_button.bind(on_release=self.calculate)
        layout.add_widget(calculate_button)

        layout.add_widget(Label(text=''))

        graphic_button = Button(text='Gráfico', font_name='Anton', font_size='20sp', size_hint=(0.4, 0.8),pos_hint={'center_x': 0.5, 'center_y': 0.5},background_color="#46244C")
        graphic_button.bind(on_press=self.popup_graphic)
        layout.add_widget(graphic_button)
        
        layout.add_widget(Label(text=f"Desenvolvido por Felipe Garcia Marçal - v{__version__}", font_size='11sp', color="#C74B50"))

        return layout


    def show_menu(self, button):
        self.dropdown.open(button)

    def on_dropdown_select(self, value):
        self.selected_fuel_label.text = value

    def on_toggle_button(self, button):
        self.selected_option = button.text

    def popup_print_result(self, text):
        popup = Popup(title="Resultado", content=Label(text=text), size_hint=(0.6, 0.6), size=(500, 500), background_color=(0,0,0,1))
        return popup.open()
    
    def popup_error(self, text):
        popup = Popup(title="Erro", content=Label(text=text), size_hint=(0.6, 0.6), size=(500, 500), background_color=(0,0,0,1))
        return popup.open()
    
    def popup_graphic(self, instance):
        graphic_button = Popup(title="", content=Image(source="grafico.png", fit_mode="fill"), size_hint=(0.7, 0.6), size=(600, 600), background_color=(0,0,0,1))
        return graphic_button.open()
    
    def return_result_txt(self,fuel, excess, co2, o2):
        return f"Combustível: {str(fuel)}\n\nExcesso de ar: {float(excess):.4f}\n\nCO2: {float(co2):.4f}\n\nO2: {float(o2):.4f}"
        
    
    def calculate(self, button):
        
        try:
            input_value = float(self.input_text.text.replace(",", "."))
            fuel = self.selected_fuel_label.text
            option = self.selected_option
            
            #fuel selection - bagasse
            if fuel == "Bagaço" and option == "Excesso de ar":
                return_co2 = interpolate(bagasse.air_excess, bagasse.co2, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=input_value)
                result = self.return_result_txt(fuel, input_value, return_co2, return_o2)
                self.popup_print_result(result)
            elif fuel == "Bagaço" and option == "CO2":
                return_excess = interpolate(bagasse.co2, bagasse.air_excess, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
                result = self.return_result_txt(fuel, return_excess, input_value, return_o2)
                self.popup_print_result(result)
            elif fuel == "Bagaço" and option == "O2":
                return_excess = interpolate(oxygen.o2, oxygen.air_excess, input_value)
                return_co2 = interpolate(x_axis=bagasse.air_excess,y_axis=bagasse.co2, value=return_excess)
                result = self.return_result_txt(fuel, return_excess, return_co2, input_value)
                self.popup_print_result(result)
            #change fuel - firewood
            elif fuel == "Lenha" and option == "Excesso de ar":
                return_co2 = interpolate(firewood.air_excess, firewood.co2, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=input_value)
                result = self.return_result_txt(fuel, excess=input_value, co2=return_co2, o2=return_o2)
                self.popup_print_result(result)
            elif fuel == "Lenha" and option == "CO2":
                return_excess = interpolate(firewood.co2, firewood.air_excess, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
                result = self.return_result_txt(fuel, excess=return_excess, co2=input_value, o2=return_o2)
                self.popup_print_result(result)
            elif fuel == "Lenha" and option == "O2":
                return_excess = interpolate(oxygen.o2, oxygen.air_excess, input_value)
                return_co2 = interpolate(x_axis=firewood.air_excess,y_axis=firewood.co2, value=return_excess)
                result = self.return_result_txt(fuel, excess=return_excess, co2=return_co2, o2=input_value)
                self.popup_print_result(result)
            #change fuel-liquid gas
            elif fuel == "GLP" and option == "Excesso de ar":
                return_co2 = interpolate(liquid_gas.air_excess, liquid_gas.co2, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=input_value)
                result = self.return_result_txt(fuel, excess=input_value, co2=return_co2, o2=return_o2)
                self.popup_print_result(result)
            elif fuel == "GLP" and option == "CO2":
                return_excess = interpolate(liquid_gas.co2, liquid_gas.air_excess, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
                result = self.return_result_txt(fuel, excess=return_excess, co2=input_value, o2=return_o2)
                self.popup_print_result(result)
            elif fuel == "GLP" and option == "O2":
                return_excess = interpolate(oxygen.o2, oxygen.air_excess, input_value)
                return_co2 = interpolate(x_axis=liquid_gas.air_excess,y_axis=liquid_gas.co2, value=return_excess)
                result = self.return_result_txt(fuel, excess=return_excess, co2=return_co2, o2=input_value)
                self.popup_print_result(result)
            #change fuel- natural gas
            elif fuel == "Gás Natural" and option == "Excesso de ar":
                return_co2 = interpolate(natural_gas.air_excess, natural_gas.co2, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=input_value)
                result = self.return_result_txt(fuel, excess=input_value, co2=return_co2, o2=return_o2)
                self.popup_print_result(result)
            elif fuel == "Gás Natural" and option == "CO2":
                return_excess = interpolate(natural_gas.co2, natural_gas.air_excess, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
                result = self.return_result_txt(fuel, excess=return_excess, co2=input_value, o2=return_o2)
                self.popup_print_result(result)
            elif fuel == "Gás Natural" and option == "O2":
                return_excess = interpolate(oxygen.o2, oxygen.air_excess, input_value)
                return_co2 = interpolate(x_axis=natural_gas.air_excess,y_axis=natural_gas.co2, value=return_excess)
                result = self.return_result_txt(fuel, excess=return_excess, co2=return_co2, o2=input_value)
                self.popup_print_result(result)
            #change fuel- oil
            elif fuel == "Óleo Pesado" and option == "Excesso de ar":
                return_co2 = interpolate(oil.air_excess, oil.co2, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=input_value)
                result = self.return_result_txt(fuel, excess=input_value, co2=return_co2, o2=return_o2)
                self.popup_print_result(result)
            elif fuel == "Óleo Pesado" and option == "CO2":
                return_excess = interpolate(oil.co2, oil.air_excess, input_value)
                return_o2 = interpolate(x_axis=oxygen.air_excess,y_axis=oxygen.o2, value=return_excess)
                result = self.return_result_txt(fuel, excess=return_excess, co2=input_value, o2=return_o2)
                self.popup_print_result(result)
            elif fuel == "Óleo Pesado" and option == "O2":
                return_excess = interpolate(oxygen.o2, oxygen.air_excess, input_value)
                return_co2 = interpolate(x_axis=oil.air_excess,y_axis=oil.co2, value=return_excess)
                result = self.return_result_txt(fuel, excess=return_excess, co2=return_co2, o2=input_value)
                self.popup_print_result(result)
        except:
            error_message = f"ERRO\n\nVerifique se o valor inserido está correto"
            self.popup_error(error_message)

    
    
LabelBase.register(name='Anton',
                fn_regular='Anton-Regular.ttf')

if __name__ == '__main__':
    CombustApp().run()
