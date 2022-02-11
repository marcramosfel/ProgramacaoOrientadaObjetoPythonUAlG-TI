from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class Contador(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        # CONTADOR
        self.label_contador = Label(font_size='20sp', markup=True, text='Contador')
        self.add_widget(self.label_contador)

        # BOX_APP > BOTÃO, CAIXA DE TEXTO, CHECKBOX
        box_app = BoxLayout(orientation='horizontal')

        # CAIXA DE TEXTO
        self.caixa_texto_contador = TextInput(multiline=False, text='0', focus=True)
        # self.caixa_texto_contador.bind(font_size='40sp') -- pesquisar como aumentar o font size em text in puts

        # BOTÃO
        self.botao_incrementar = Button(font_size='20sp', markup=True, text = '[b][color=#000]decrementar[/color][/b]',
                                        background_color=[139, 0, 0, 1])
        self.botao_incrementar.bind(on_release = self.incrementar)

        # CHECKBOX
        self.check_para_ativar = CheckBox()
        self.check_para_ativar.bind(active=self.esta_ativo)



        box_app.add_widget(self.botao_incrementar)
        box_app.add_widget(self.caixa_texto_contador)
        box_app.add_widget((self.check_para_ativar))
        self.add_widget(box_app)

    def esta_ativo(self, instance, value):
        if instance == self.check_para_ativar:
            print(value)
            if value == True:
                self.botao_incrementar.background_color = [0, 128, 0, 1]
                self.botao_incrementar.text = '[b][color=#000]incrementar[/color][/b]'
            else:
                self.botao_incrementar.background_color=[139, 0, 0, 1]
                self.botao_incrementar.text = '[b][color=#000]decrementar[/color][/b]'

    def incrementar(self, instance):
        if instance == self.botao_incrementar:
            if self.check_para_ativar.active:

                digito = int(self.caixa_texto_contador.text)
                # print(type(digito))
                digito += 1
                self.caixa_texto_contador.text = str(digito)
            else:
                digito = int(self.caixa_texto_contador.text)
                # print(type(digito))
                digito -= 1
                self.caixa_texto_contador.text = str(digito)

class MyApp(App):
    def build(self):
        return Contador()


MyApp().run()
