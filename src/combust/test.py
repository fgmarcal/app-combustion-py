from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton


class MainPage(PageLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.create_page1()
        self.create_page2()
        self.create_page3()
        self.border = 40
        

    def create_page1(self):
        self.background_color = "#CDC2AE"
        page1 = GridLayout(cols=1)
        buttons = ["Bagaço", "Lenha", "GLP", "Gás Natural", "Óleo Pesado"]
        for button_text in buttons:
            button = ToggleButton(text=button_text, group="combust", background_color='#17594A')
            page1.add_widget(button)
        self.add_widget(page1)

    def create_page2(self):

        page2 = GridLayout(cols=1)
        buttons = ["Excesso de ar", "CO2", "O2"]
        for button_text in buttons:
            button = ToggleButton(text=button_text, group="gas", background_color='#CDC2AE')
            page2.add_widget(button)
        self.add_widget(page2)

    def create_page3(self):

        page3 = GridLayout(rows=3)
        input_layout = GridLayout(cols=3)
        input_label = Label(text="Digite valor de entrada:")
        self.input_number = TextInput(multiline=False)
        input_layout.add_widget(input_label)
        input_layout.add_widget(self.input_number)
        calculate_button = Button(text="Calcular", on_release=self.calculate, background_color='#17594A')
        table_layout = GridLayout(cols=3)
        headers = ["1", "2", "3"]
        values = ["x", "y", "z"]
        for header in headers:
            table_layout.add_widget(Label(text=header))
        for value in values:
            table_layout.add_widget(Label(text=value))
        page3.add_widget(input_layout)
        page3.add_widget(calculate_button)
        page3.add_widget(table_layout)
        self.add_widget(page3)

    def calculate(self, *args):
        number = self.input_number.text
        # Faça o cálculo com o número fornecido


class MyApp(App):
    def build(self):
        return MainPage()


if __name__ == '__main__':
    MyApp().run()
