from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class Inversa(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        """# grid = GridLayout(cols=2)"""

        # Se a ocorrência tem foco no momento.
        # Defini-lo como True se ligará e/ou solicitará o teclado, e a entrada será encaminhada para a instância.
        # Defini-lo como False irá desvincular e/ou liberar o teclado.
        # Para um determinado teclado, apenas um widget pode ter seu foco, então o foco um irá automaticamente
        # desfocar a outra instância segurando seu foco.

        self.caixa_texto_normal = TextInput(text="", multiline=False)
        self.caixa_texto_normal.bind(on_text_validate=self.on_enter)
        self.caixa_texto_inversa = TextInput(multiline=False)

        box = BoxLayout(orientation='horizontal')
        box.add_widget(self.caixa_texto_normal)
        box.add_widget(self.caixa_texto_inversa)

        """#grid.add_widget(box)"""

        self.add_widget(box)

    def on_enter(self, instance):
        if instance == self.caixa_texto_normal:
            print('The widget', instance, 'has')
            palavra_anchor = instance.text[::-1]
            print(palavra_anchor)
            self.caixa_texto_inversa.text = palavra_anchor


class MyApp(App):
    def build(self):
        return Inversa()


MyApp().run()
