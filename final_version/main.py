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
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
from fuel import FUEL_LIST, OPTION_LIST, Fuel

kivy.require('2.0.0')

__version__ = '1.0.11'

LabelBase.register(name='Anton', fn_regular='Anton-Regular.ttf')

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
        fuels = FUEL_LIST
        for fuel in fuels:
            btn = Button(text=fuel, size_hint_y=None, height=70, font_name='Anton', font_size='18sp', background_color="#C74B50")
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            btn.bind(on_release=lambda btn: self.on_dropdown_select(value=btn.text))
            self.dropdown.add_widget(btn)

        self.selected_fuel_label = Label(text='', font_name='Anton', font_size='30sp', color="#890F0D")
        layout.add_widget(self.selected_fuel_label)

        white_space = Label(text='')
        layout.add_widget(white_space)

        self.input_text = TextInput(hint_text='Insira um valor:', font_name='Anton', font_size='19sp',
                                    multiline=False, input_type='number', size_hint=(0.5, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.input_text)


        layout.add_widget(Label(text="Selecione o tipo de entrada:", font_name='Anton', font_size='30sp', color="#C74B50"))
        toggle_button = ToggleButton(text=str(OPTION_LIST[0]), font_name='Anton', font_size='20sp', group='options', size_hint_y=0.5, background_color="#C2DEDC")
        toggle_button.bind(on_press=self.on_toggle_button)
        layout.add_widget(toggle_button)

        toggle_button = ToggleButton(text=str(OPTION_LIST[1]), font_name='Anton', font_size='20sp', group='options', size_hint_y=0.5, background_color="#C2DEDC")
        toggle_button.bind(on_press=self.on_toggle_button)
        layout.add_widget(toggle_button)

        toggle_button = ToggleButton(text=str(OPTION_LIST[2]), font_name='Anton', font_size='20sp', group='options', size_hint_y=0.5, background_color="#C2DEDC")
        toggle_button.bind(on_press=self.on_toggle_button)
        layout.add_widget(toggle_button)

        white_space2 = Label(text='')
        layout.add_widget(white_space2)

        calculate_button = Button(text='Calcular', font_name='Anton', font_size='20sp', size_hint=(0.4, 0.8),pos_hint={'center_x': 0.5, 'center_y': 0.5},background_color="#C74B50")
        calculate_button.bind(on_release=self.calculate)
        layout.add_widget(calculate_button)

        white_space3 = Label(text='')
        layout.add_widget(white_space3)

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
    
    def calculate(self, button):
        
        try:
            input_value = float(self.input_text.text.replace(",", "."))
            selected_fuel_text = self.selected_fuel_label.text
            option = self.selected_option

            fuel = Fuel(fuel=selected_fuel_text, option=option)
            result = fuel.return_options(input_value)
            self.popup_print_result(result)

        except Exception as err:
            print(err)
            error_message = "ERRO\n\nVerifique se o valor inserido está correto"
            self.popup_error(error_message)

    
    


if __name__ == '__main__':
    CombustApp().run()
