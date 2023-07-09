from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class InterpolationApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.x_data = [1.511751399, 6.336151369, 11.66438714, 17.23860761, 23.82575235, 29.39424786, 34.95897902, 40.52488655, 46.0882845, 52.08220776, 57.20708116, 62.76561683, 68.32634837, 73.87845327, 79.43573415, 84.99113286, 90.54496309, 96.09785223, 101.6515256, 107.2047284, 112.7566765, 118.3083109, 123.8597884, 129.4109522, 134.9624297, 140.6646538, 146.0616203, 149.3411548]
        self.y_data = [11.70439524, 11.13516103, 10.56549114, 10.08392915, 9.523301127, 9.126964573, 8.786666667, 8.428856683, 8.108405797, 7.807439614, 7.586586151, 7.338518519, 7.057761675, 6.905426731, 6.676038647, 6.474669887, 6.296650564, 6.132640902, 5.956956522, 5.788276973, 5.638276973, 5.49294686, 5.349951691, 5.211626409, 5.06863124, 4.931521739, 4.838679549, 4.767342995]

    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text='Valor de x:')
        self.text_input = TextInput()
        button = Button(text='Calcular', on_press=self.calculate)
        self.result_label = Label(text='')

        layout.add_widget(label)
        layout.add_widget(self.text_input)
        layout.add_widget(button)
        layout.add_widget(self.result_label)
        

        return layout

    def calculate(self, instance):
        try:
            x = float(self.text_input.text)
            resultado = self.polinomioInterpolacao(x)
            self.result_label.text = f'Resultado: {resultado}'
        except ValueError:
            self.result_label.text = 'Digite um valor numérico válido'

    def polinomioInterpolacao(self, x):
        n = len(self.x_data)
        resultado = 0

        for i in range(n):
            termo = self.y_data[i]
            for j in range(n):
                if j != i:
                    termo *= (x - self.x_data[j]) / (self.x_data[i] - self.x_data[j])
            resultado += termo

        return resultado


if __name__ == '__main__':
    InterpolationApp().run()
