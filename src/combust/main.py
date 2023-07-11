from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from engine import interpolate
import bagasse
import natural_gas
import firewood
import liquid_gas
import oil
import oxygen


class InterpolationApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.x_data = oil.air_excess
        self.y_data = oil.co2
    
    def build(self):
        layout = BoxLayout(orientation='vertical')

        select = Label(text="Selecione qual é o tipo do valor inserido")

        excess = ToggleButton(text="Excesso de ar", group="combust", on_press=self.excess)
        carbonBioxyde = ToggleButton(text="CO2", group="combust", on_press=self.co2)
        ox2 = ToggleButton(text="Oxigênio", group="combust")

        label = Label(text='Insira o valor:')
        self.text_input = TextInput()
        button = Button(text='Calcular', on_press=self.calculate)
        self.result_label = Label(text='')
        clear_btn = Button(text='Limpar', on_press=self.clear)

        layout.add_widget(select)

        layout.add_widget(excess)
        layout.add_widget(carbonBioxyde)
        layout.add_widget(ox2)

        layout.add_widget(label)
        layout.add_widget(self.text_input)
        layout.add_widget(button)
        layout.add_widget(self.result_label)
        layout.add_widget(clear_btn)
        
        return layout


    def calculate(self, instance):
        try:
            value = float(self.text_input.text)
            resultado = interpolate(self.x_data, self.y_data, value)
            self.result_label.text = f'Resultado: {resultado}'
        except ValueError:
            self.result_label.text = 'Digite um valor numérico válido'
    
    def clear(self, instance):
        self.result_label.text = ''
        self.value = 0
    
    def excess(self, instance):
        self.x_data = bagasse.air_excess
        self.y_data = bagasse.co2

    def co2(self, instance):
        self.x_data = bagasse.co2
        self.y_data = bagasse.air_excess



if __name__ == '__main__':
    InterpolationApp().run()
