from kivy.app import App
from kivy.uix.boxlayout import BoxLayout



class Galo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.jogada = 0
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        # self.poe_no_board()
        self.posicoes= ([self.ids.posicao1, self.ids.posicao2, self.ids.posicao3],
                        [self.ids.posicao4, self.ids.posicao5, self.ids.posicao6],
                        [self.ids.posicao7, self.ids.posicao8, self.ids.posicao9])


    def ganhou(self):
        # checando linhas
        for i in range(3):
            soma = self.board[i][0] + self.board[i][1] + self.board[i][2]
            if soma == 3 or soma == -3:
                self.board = [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]
                return 1

        # checando colunas
        for i in range(3):
            soma = self.board[0][i] + self.board[1][i] + self.board[2][i]
            if soma == 3 or soma == -3:
                self.board = [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]
                return 1


        # checando diagonais
        diagonal1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
        diagonal2 = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:

            self.board = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]
            return 1

        return 0

    def modifica_board(self):
        for i in range(len(self.posicoes)):
            for k in range(len(self.posicoes[i])):
                if self.posicoes[k][i].text == '[b][color=#2e8b57]X[/color][/b]':
                    self.board[k][i] = 1


                elif self.posicoes[k][i].text == '[b][color=#fa1603]O[/color][/b]':
                    self.board[k][i] = -1


                elif self.posicoes[k][i].text == ' ':
                    self.board[k][i] = 0

        print(self.board)

    def muda_placar(self, jogador):
        if jogador == 1:
              atual = int(self.ids.jogador1.text)
              atual +=1
              self.ids.jogador1.text = str(atual)
        elif jogador == 0:
            atual = int(self.ids.jogador2.text)
            atual += 1
            self.ids.jogador2.text = str(atual)

    def poe_no_board(self, value):
        for k in range(3):
            for i in self.posicoes[k]:
                if i == value:
                    if i.text == ' ':
                        i.text = ['[b][color=#2e8b57]X[/color][/b]', '[b][color=#fa1603]O[/color][/b]'][self.jogada%2]
                        i.background_color = ["#90ee90", "#ff4040"][self.jogada%2]

                        self.jogada +=1

        self.modifica_board()
        if self.ganhou() == 1:
            print('ganhou')
            self.muda_placar(self.jogada % 2)
            for k in range(3):
                for i in self.posicoes[k]:
                    i.text = ' '
                    i.background_color = [255,255,255,1]
            self.jogada = 0
        if self.jogada == 9:
            print('empate')
            for k in range(3):
                for i in self.posicoes[k]:
                    i.text = ' '
                    i.background_color = [255, 255, 255, 1]
            self.jogada = 0

        print(self.jogada)


class JogoDoGaloApp(App):
    def build(self):
        return Galo()


JogoDoGaloApp().run()
