from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class TextosInversosNaoInversos(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2

        box_textos = BoxLayout(orientation='vertical')

        self.caixa_texto_normal = TextInput(multiline=False)
        self.caixa_texto_normal.bind(text=self.on_text)
        self.caixa_texto_inversa = TextInput(multiline=False)
        self.caixa_texto_inversa.bind(text=self.on_text)

        box_textos.add_widget(self.caixa_texto_normal)
        box_textos.add_widget(self.caixa_texto_inversa)

        self.add_widget(box_textos)

        self.label_verde_vermelho = Label(font_size='20sp', markup=True, color=[0,50,50,1])

        self.add_widget(self.label_verde_vermelho)

    def on_text(self, instance, value):
        if instance == self.caixa_texto_normal:
            print('The widget', instance, 'has', value)
            palavra_anchor1 = value  # faço isso para nao dar erro de subscritable!!
            print(palavra_anchor1)
            if palavra_anchor1[::-1] == self.caixa_texto_inversa.text:
                self.label_verde_vermelho.text = '[b][color=#228b22]TEXTOS INVERSOS[/color][/b]'

            else:
                self.label_verde_vermelho.text = '[b][color=#ff0000]TEXTOS NÃO INVERSOS[/color][/b]'
        elif instance == self.caixa_texto_inversa:
            print('The widget', instance, 'has', value)
            palavra_anchor1 = value
            print(palavra_anchor1)
            if palavra_anchor1[::-1] == self.caixa_texto_normal.text:
                self.label_verde_vermelho.text = '[b][color=#228b22]TEXTOS INVERSOS[/color][/b]'
            else:
                self.label_verde_vermelho.text = '[b][color=#ff0000]TEXTOS NÃO INVERSOS[/color][/b]'


class MyApp(App):
    def build(self):
        return TextosInversosNaoInversos()


MyApp().run()
