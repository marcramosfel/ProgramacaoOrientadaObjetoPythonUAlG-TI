from abc import ABC, abstractmethod
import random

#apenas adaptei o jogo do galo que esta na lista para as regras do 4 em linha

class Jogo(ABC) :
    """ implementa uma classe para um jogo com 2 humanos """

    def __init__(self) :
        print('bom jogo ... ')
        self.inicializa_tabuleiro()

    @abstractmethod
    def joga_humano(self, jogador) :
        """ metodo que solicita ao humano : jogador : a proxima jogada e coloca -a no tabuleiro
        : param jogador : numero do jogador (0 ou 1)
        """
        pass

    @abstractmethod
    def terminou(self) :
        """ devolve ‘True ‘ se foi verificada a condicao de paragem , i.e. , um jogador ganhou .
        devolve ‘False ‘ caso contrario """
        pass

    @abstractmethod
    def mostra_tabuleiro(self) :
        """ desenha o tabuleiro """
        pass

    @abstractmethod
    def inicializa_tabuleiro(self) :
        """ inicializa o tabuleiro de jogo """
        pass

    @abstractmethod
    def ha_jogadas_possiveis(self) :
        """ verifica se ainda ha jogadas possiveis ou se o jogo esta empatado """
        pass

    def jogar(self) :
        """ corre o jogo ... """
        jogador = random.randint(0, 1)
        while True :
            self.mostra_tabuleiro()
            self.joga_humano(jogador)
            if self.terminou() :
                self.mostra_tabuleiro()
                print(f'o jogador {jogador} ganhou !! ')
                return
            elif not self.ha_jogadas_possiveis() :
                print(f'Empataram !!! ')
                return
            jogador = (jogador + 1) % 2


class QuatroLinha(Jogo) :

    def inicializa_tabuleiro(self) :
        self.numero_de_jogadas_realizadas = 0  # conta as jogadas , serve para saber se ainda ha jogadas validas
        self.tabuleiro = {(l, c) : ' ' for l in range(8) for c in range(8)}  # o tabuleiro e um dicionario !
        #print(self.tabuleiro)
    def _le_linha_coluna_valida(self, s) :
        """ metodo auxiliar para ler uma posicao que seja 0, 1 ou 2 ..."""
        while True :
            x = input(s)
            if x in ['0', '1', '2', '3', '4', '5', '6', '7'] :
                return int(x)

    def joga_humano(self, jogador) :
        self.jogador = jogador
        print(f'jogador {self.jogador} insira a sua jogada ')
        while True :
            #self.linha = self._le_linha_coluna_valida('Linha ?')
            self.coluna = self._le_linha_coluna_valida('Coluna ?')

            for i in range(7, -1, -1):
                if self.tabuleiro[(i, self.coluna)] == ' ':  # verifica se a posicao nao esta preenchida , i.e., e valida
                    self.tabuleiro[(i, self.coluna)] = ['X', 'O'][self.jogador]
                    self.numero_de_jogadas_realizadas += 1
                    return
            else:
                print('Coluna cheia, tente outra')

    def terminou(self) :
        for l in range(8) :  #
            for c in range(5) :
                for k in range(0, 4) :

                    if not self.tabuleiro[(l, c + k)] == ['X', 'O'][self.jogador]:
                       # print(self.tabuleiro[(l,c)])
                        break
                else:
                    return True
        for c in range(8) :
            for l in range(5) :
                for k in range(0, 4) :
                    if not self.tabuleiro[(l + k, c)] == ['X', 'O'][self.jogador]:
                        break
                else:  
                    return True

        """
        for c in range(8):
            for l in range(5):
                for k in range(4):
                    if not self.tabuleiro[(c+k, l+k)] == ['X', 'O'][self.jogador]:
                        break
                else:
                    return"""

    def mostra_tabuleiro(self) :
        print(25 * '--')
        for l in range(8) :
            for c in range(8) :
                print(f' | {self.tabuleiro[(l, c)]} ', end=' ')
            print(' | \n' + 25 * '--')

    def ha_jogadas_possiveis(self) :
        return self.numero_de_jogadas_realizadas < 64


quatrolinha = QuatroLinha()
quatrolinha.jogar()
