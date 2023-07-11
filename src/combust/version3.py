from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        self.add_widget(
            Label(
                text="COMBUSTÃO",
                font_name='Roboto', font_size='50sp', color="#E57C23",
                size_hint=(.5, .1),
                pos_hint={'center_x': 0.5, 'center_y': 0.9}))
        
        self.add_widget(
            Button(text='Selecionar Combustível', font_name='Roboto',
                    font_size='20sp', size_hint=(1, 0.5),
                    background_color="#E57C23",
                    pos_hint={'center_x': 0.5, 'center_y': 0.7})
        )
        self.dropdown = DropDown()
        fuels = ["Bagaço", "Lenha", "GLP", "Gás Natural", "Óleo Pesado"]
        for fuel in fuels:
            btn = Button(text=fuel, size_hint_y=None, height=50, font_name='Roboto', font_size='18sp', background_color="#025464")
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            btn.bind(on_release=lambda btn: self.on_dropdown_select(value=btn.text))
            self.dropdown.add_widget(btn)


class CombustApp(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(*get_color_from_hex("#3C486B"))
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    CombustApp().run()