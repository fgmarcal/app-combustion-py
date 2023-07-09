from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.dropdown import DropDown
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
        self.x_data = bagasse.air_excess
        self.y_data = bagasse.co2
        self.value = 0
        self.calculator = interpolate(self.x_data, self.y_data, self.value)

    def build(self):
        layout = BoxLayout(orientation='vertical')

        select = Label(text="Selecione qual é o tipo do valor inserido")

        excess = ToggleButton(text="Excesso de ar", group="combust")
        carbonBioxyde = ToggleButton(text="CO2", group="combust")
        ox2 = ToggleButton(text="Oxigênio", group="combust")

        dropdown = DropDown()

        label = Label(text='Insira o valor:')
        self.text_input = TextInput()
        button = Button(text='Calcular', on_press=self.calculate)
        self.result_label = Label(text='')

        layout.add_widget(select)
        
        layout.add_widget(excess)
        layout.add_widget(carbonBioxyde)
        layout.add_widget(ox2)

        layout.add_widget(label)
        layout.add_widget(self.text_input)
        layout.add_widget(button)
        layout.add_widget(self.result_label)
        

        return layout

    def calculate(self, instance):
        try:
            self.value = float(self.text_input.text)
            resultado = self.calculator
            self.result_label.text = f'Resultado: {resultado}'
        except ValueError:
            self.result_label.text = 'Digite um valor numérico válido'



if __name__ == '__main__':
    InterpolationApp().run()
