from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class TrocaPalavrass(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        box_textos = BoxLayout(orientation='horizontal')

        self.caixa_texto_esquerda = TextInput(multiline=False, text='Esquerda')
        self.caixa_texto_direita = TextInput(multiline=False, text='Direita')


        box_textos.add_widget(self.caixa_texto_esquerda)
        box_textos.add_widget(self.caixa_texto_direita)

        self.add_widget(box_textos)

        self.botao_troca= Button(text='[b][color=#000]Trocar Palavras[/color][/b]',
                                 font_size='20sp', markup=True, background_color=[0,139,139, 1])
        self.botao_troca.bind(on_release = self.troca_palavras)
        self.add_widget(self.botao_troca)

    def troca_palavras(self, instance):
        if instance == self.botao_troca:
            direita = self.caixa_texto_direita.text
            esquerda = self.caixa_texto_esquerda.text
            print(esquerda, direita)
            self.caixa_texto_esquerda.text = direita
            self.caixa_texto_direita.text = esquerda

    # def on_text(self, instance, value):
    #     if instance == self.caixa_texto_esquerda:
    #         print('The widget', instance, 'has', value)
    #     elif instance == self.caixa_texto_direita:
    #         print('The widget', instance, 'has', value)



class MyApp(App):
    def build(self):
        return TrocaPalavrass()


MyApp().run()
