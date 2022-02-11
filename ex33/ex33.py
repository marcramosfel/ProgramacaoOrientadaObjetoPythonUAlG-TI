class Conta:
    def __init__(self, dono, taxa_de_juro=0, saldo=0):
        self.dono = dono
        self.taxa_de_juro = taxa_de_juro
        self.saldo = saldo

    @property
    def dono(self):
        return self._dono

    @dono.setter
    def dono(self, value):
        """ Guarda uma string formatada em " title " (e.g., ’luigi vercotti ’ -> ’Luigi
        Vercotti )"""
        self._dono = value.title()
        #self._dono = value

    @property
    def taxa_de_juro(self):
        """ devolve a taxa de juro """
        return self._taxa_de_juro

    @taxa_de_juro.setter
    def taxa_de_juro(self, value):
        """ Guarda a taxa de juro . Deve ser float ou int em percentagem (0 -100%) .
        A taxa_de_juro e nao negativa , sendo que se for fornecido um valor negativo a
        taxa_de_juro e colocada a 0.

        """
        try:
            """if isinstance(value, float)== False or isinstance(value, int) == False:
                raise Exception(value, 'O valor tem de ser um número inteiro ou float')"""
            if isinstance(value, float) and value > 0 and value < 1:
                self._taxa_de_juro = value
            elif isinstance(value, int) and value > 1:
                self._taxa_de_juro = value / 100
            elif value < 0:
                self._taxa_de_juro = value * 0

        except Exception as err:
            print(err)

    @property
    def saldo(self):
        """ Devolve o saldo """
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        """ Guarda ao saldo . Deve ser float ou int. O Saldo e nao negativa , sendo que
        se for fornecido um valor negativo o saldo e colocada a 0.
        """
        if isinstance(value, int) or isinstance(value, float):
            self._saldo = value
        if value < 0:
            self._saldo = 0

    def capitaliza(self):
        """ Acresencenta os juros ao saldo .
        E.g., se saldo = 1000 e taxa_juro = 2 entao saldo passa a 1020
        """
        self._saldo = self._saldo + (self._saldo * self._taxa_de_juro)
        return self._saldo

    def cobra_comissao(self, comissao):
        """ o valor da comissao e retirado ao saldo .
        Se o saldo for maior do que a comissao entao cobra tudo , senao cobra o
        equivalente ao existente em saldo . E.g.:
        saldo = 10 e comissao = 5 -> saldo = 5 e cobrado = 5
        saldo = 10 e comissao = 15 -> saldo = 0 e cobrado = 10
        : ensures : valor descontado ao saldo
        """
        if self._saldo > comissao:
            self._saldo = self._saldo - comissao
            cobrado = comissao
        else:
            cobrado = self._saldo
            self._saldo = 0

        return cobrado

    def faz_levantamento(self, valor):
        """ Subtrai ao saldo o valor desde que o saldo se mantenha positivo .
        : ensures : True se o levantamento foi possivel , False caso contrario
        """
        if self._saldo - valor > 0:
            self._saldo -= valor
            return True
        else:
            return False

    def faz_deposito(self, valor):
        """ Acrescenta ao saldo o valor """
        self.saldo += valor
        return self.saldo

