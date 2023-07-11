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

class CombustApp(App):
    def build(self):
        super().build()
        layout = BoxLayout(orientation='vertical', size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        Window.clearcolor = (get_color_from_hex('#AAE3E2'))

        header_label = Label(text='COMBUSTÃO', font_name='Anton', font_size='50sp', color="#E57C23")
        layout.add_widget(header_label)

        menu_button = Button(text='Selecionar Combustível', font_name='Anton', font_size='20sp', size_hint=(1, 0.8) , background_color="#E57C23")
        menu_button.bind(on_release=self.show_menu)
        layout.add_widget(menu_button)

        self.dropdown = DropDown()
        fuels = ["Bagaço", "Lenha", "GLP", "Gás Natural", "Óleo Pesado"]
        for fuel in fuels:
            btn = Button(text=fuel, size_hint_y=None, height=50, font_name='Anton', font_size='18sp', background_color="#F2CD5C")
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            btn.bind(on_release=lambda btn: self.on_dropdown_select(value=btn.text))
            self.dropdown.add_widget(btn)

        self.selected_fuel_label = Label(text='', font_name='Anton', font_size='30sp', color="#F6830F")
        layout.add_widget(self.selected_fuel_label)

        self.blank_space_1 = Label(text='')
        layout.add_widget(self.blank_space_1)

        self.input_text = TextInput(hint_text='Insira um valor numérico', font_name='Anton', font_size='19sp',
                                    multiline=False, input_type='number', size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.input_text)

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

        self.popup = Popup(title="", content=Label(text='resultado'), size_hint=(None, None), size=(400, 400))

        calculate_button = Button(text='Calcular', font_name='Anton', font_size='20sp', size_hint=(0.2, 0.8),pos_hint={'center_x': 0.5, 'center_y': 0.5},background_color="#4F709C")
        calculate_button.bind(on_release=self.calculate)
        layout.add_widget(calculate_button)



        return layout

    def show_menu(self, button):
        self.dropdown.open(button)

    def on_toggle_button(self, button):
        self.selected_option = button.text

    def calculate(self, button):
        value = self.input_text.text
        fuel = self.selected_fuel_label.text
        option = self.selected_option
        button = self.popup.open()
        # Lógica de cálculo com os valores selecionados

    def on_start(self):
        self.selected_option = 'Excesso de ar'

    def on_dropdown_select(self, value):
        self.selected_fuel_label.text = value
    
LabelBase.register(name='Anton',
                fn_regular='Anton-Regular.ttf')

if __name__ == '__main__':
    CombustApp().run()
