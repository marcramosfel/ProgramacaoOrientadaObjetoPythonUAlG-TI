import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

valor = str(random.randint(0, 100))
print(valor)
class Contador(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        # CONTADOR
        self.label_contador = Label(font_size='20sp', markup=True, text='ADIVINHAÇÃO\nColoque um número entre 0 e 100')
        self.add_widget(self.label_contador)

        # BOX_APP > BOTÃO, CAIXA DE TEXTO, LABEL
        box_app = BoxLayout(orientation='horizontal')


        # BOTÃO
        self.botao_adivinhar = Button(font_size='17sp', markup=True, text=f'[b][color=#000]Submeter Adivinhação\n>clique aqui[/color][/b]',
                                        background_color=[1, 177, 122, 1])
        self.botao_adivinhar.bind(on_release=self.adivinhar)

        # CAIXA DE TEXTO
        self.caixa_texto_password = TextInput(multiline=False, password=True, text=valor, focus = True)
        self.caixa_texto_normal = TextInput(multiline=False, text='')


        #LABEL
        self.mostrar_resultado = Label(text='TENTE ADIVINHAR', markup=True)

        box_app.add_widget(self.botao_adivinhar)
        box_app.add_widget(self.caixa_texto_normal)
        box_app.add_widget(self.caixa_texto_password)
        box_app.add_widget(self.mostrar_resultado)
        self.add_widget(box_app)

    def adivinhar(self, instance):
        if instance == self.botao_adivinhar:
            texto = self.caixa_texto_normal.text
            password = int(self.caixa_texto_password.text)
            if texto.isdigit():
                texto = int(texto)
                if texto == password:
                    print('iguais')
                    self.mostrar_resultado.text = '[b][color=#2e8b57]PARABENS ACERTOU![/color][/b]'
                    self.caixa_texto_password.password = False
                elif texto < password:
                    self.mostrar_resultado.text = '[b][color=#fde910]TENTA UM VALOR MAIOR![/color][/b]'
                elif texto > password:
                    self.mostrar_resultado.text = '[b][color=#fde910]TENTA UM VALOR MENOR![/color][/b]'
            else:
                self.mostrar_resultado.text = '[b][color=#fa1603]INSIRA UM NUMERO[/color][/b]'

            print(texto, password)


class MyApp(App):
    def build(self):
        return Contador()


MyApp().run()
