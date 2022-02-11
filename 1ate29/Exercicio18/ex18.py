class Pessoa:
    def __init__(self, nome, endereco, telefone) :
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def __repr__(self) :
        return f'\nA pessoa chama-se {self.nome}, mora em {self.endereco}, e tem o numero {self.telefone}'


    @property
    def nome(self) :
        return self.__nome

    @nome.setter
    def nome(self, nome) :
        self.__nome = nome

    @property
    def endereco(self) :
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco) :
        self.__endereco = endereco

    @property
    def telefone(self) :
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone) :
        self.__telefone = telefone

class Fornecedor(Pessoa) :

    def __init__(self, nome, endereco, telefone, valor_credito, valor_divida) :
        super().__init__(nome=nome, endereco=endereco, telefone=telefone)
        self.valor_divida = valor_divida
        self.valor_credito = valor_credito

    def __repr__(self) :
        return f'{Pessoa.__repr__(self)} \nTem um valor de credito de {self.valor_credito}, e valor de divida de {self.valor_divida}.'

    @property
    def valor_divida(self) :
        return self.__valor_divida

    @valor_divida.setter
    def valor_divida(self, valor_divida) :
        self.__valor_divida = valor_divida

    @property
    def valor_credito(self) :
        return self.__valor_credito

    @valor_credito.setter
    def valor_credito(self, valor_credito) :
        self.__valor_credito = valor_credito

    @classmethod
    def obter_saldo(cls, valor_credito, valor_divida) :
        total = valor_credito - valor_divida
        return total

class Empregado(Pessoa) :

    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto) :
        super().__init__(nome=nome, endereco=endereco, telefone=telefone)
        self.codigo_setor = codigo_setor
        self.salario_base = salario_base
        self.imposto = imposto

    def __repr__(self) :
        return f'{Pessoa.__repr__(self)} \nTem um código de setor de {self.codigo_setor}, um salário base de {self.salario_base}, e um imposto de {self.imposto}'

    @property
    def codigo_setor(self) :
        return self.__codigo_setor

    @codigo_setor.setter
    def codigo_setor(self, codigo_setor) :
        self.__codigo_setor = codigo_setor

    @property
    def salario_base(self) :
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base) :
        self.__salario_base = salario_base

    @property
    def imposto(self) :
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto) :
        self.__imposto = imposto


    def calcular_salario(self, salario_base, imposto) :
        salario = round(salario_base * (1 - imposto))
        return salario

class Admnistrador(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, ajuda_de_custo) :
        super().__init__(nome=nome, endereco=endereco, telefone=telefone, codigo_setor=codigo_setor, salario_base = salario_base, imposto = imposto)
        self.ajuda_de_custo = ajuda_de_custo

    def __repr__(self) :
        return  f'{Empregado.__repr__(self)}, mas como é um administrador tem uma ajuda de custo de {self.ajuda_de_custo}'


    @property
    def ajuda_de_custo(self):
        return self.__ajuda_de_custo

    @ajuda_de_custo.setter
    def ajuda_de_custo(self, ajuda_de_custo):
        self.__ajuda_de_custo = ajuda_de_custo

    def calcular_salario(self, salario_base, imposto, ajuda_de_custo=None):
        super(Admnistrador, self).calcular_salario(salario_base, imposto)
        salario = round(salario_base * (1 - imposto)) + ajuda_de_custo
        return salario

class Operario (Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, valor_producao, comissao) :
        super().__init__(nome=nome, endereco=endereco, telefone=telefone, codigo_setor=codigo_setor, salario_base=salario_base, imposto=imposto)
        self.valor_producao = valor_producao
        self.comissao = comissao

    def __repr__(self):
        return f'{Empregado.__repr__(self)}, produziu {self.valor_producao} euros, e ganhou uma comissao de {self.comissao}, totalizando assim ' \
               f'{self.comissao * self.valor_producao} euros em comissões'

    @property
    def valor_producao(self):
        return self.__valor_producao

    @valor_producao.setter
    def valor_producao(self, valor_producao):
        self.__valor_producao = valor_producao

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, comissao):
        self.__comissao = comissao

    def calcular_salario(self, salario_base, imposto, valor_producao = None, comissao = None):
        super(Operario, self).calcular_salario(salario_base, imposto)
        salario = round(salario_base * (1 - imposto)) + round(valor_producao*comissao)
        return salario

class Vendedor (Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, valor_vendas, comissao) :
        super().__init__(nome=nome, endereco=endereco, telefone=telefone, codigo_setor=codigo_setor, salario_base=salario_base, imposto=imposto)
        self.valor_vendas = valor_vendas
        self.comissao = comissao

    def __repr__(self):
        return f'{Empregado.__repr__(self)}, vendeu {self.valor_vendas} euros, e ganhou uma comissao de {self.comissao}, totalizando assim ' \
               f'{self.comissao * self.valor_vendas} euros em comissões'

    @property
    def valor_vendas(self):
        return self.__valor_vendas

    @valor_vendas.setter
    def valor_vendas(self, valor_vendas):
        self.__valor_vendas = valor_vendas

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, comissao):
        self.__comissao = comissao

    def calcular_salario(self, salario_base, imposto, valor_vendas = None, comissao = None):
        super(Vendedor, self).calcular_salario(salario_base, imposto)
        salario = round(salario_base * (1 - imposto)) + round(valor_vendas*comissao)
        return salario
    
def main_pessoa():

    nome = input('NOME: ')
    endereco = input('ENDERECO: ')
    telefone = input('TELEFONE: ')

    """nome = 'Marcos'
    endereco = 'Faro'
    telefone = '2134'"""
    return nome, endereco, telefone

def main_fornecedor(person) :
    valor_credito = int(input('CREDITO: '))
    valor_divida = int(input('DIVIDA: '))
    """valor_credito = 1000
    valor_divida = 100"""

    forn = Fornecedor(person[0], person[1], person[2], valor_credito, valor_divida)
    print(forn.__repr__() + f'\nO valor do saldo é de {forn.obter_saldo(forn.valor_credito, forn.valor_divida)}')

def main_empregado(person) :

    """codigo_setor = '120'
    salario_base = 1000
    imposto = 0.07"""
    codigo_setor = input('Digite o código do setor do Empregado:')
    while True:
        salario_base = input('Digite o salario base : ')
        imposto = input('Digite o imposto sendo um float entre 0 e 1: ')
        if imposto.replace('.', '', 1).isdigit() and salario_base.replace('.', '', 1).isdigit():
            if float(imposto) > 0.0 and float(imposto) < 1.0:
                imposto = float(imposto)
                salario_base = float(salario_base)
                break
            else:
                print('Imposto tem que ser float entre 0 e 1 e o Salario tem que ser um numero')
        else:
            print('Imposto tem que ser float entre 0 e 1')
            continue

    empregado = Empregado(person[0], person[1], person[2], codigo_setor, salario_base, imposto)
    repr = empregado , f'.\nO salario total assim do {empregado.nome} é de {empregado.calcular_salario(salario_base, imposto)}!'
    salario_empregado = empregado.calcular_salario(salario_base, imposto)
    #print(salario_empregado)
    return person[0], person[1], person[2], codigo_setor,  salario_base, imposto, salario_empregado, empregado, repr

def main_administrador(empreg):

    while True:
        ajuda_de_custo = input('Digite o valor da ajuda de custo?')
        if ajuda_de_custo.replace('.','', 1).isdigit():
            ajuda_de_custo = float(ajuda_de_custo)
            break
        else:
            print('A ajuda de custo tem que ser um float') #Pode ser que a ajuda de custo seja com centimos
            continue


    """ajuda_de_custo = 100"""
    adm = Admnistrador(empreg[0], empreg[1], empreg[2], empreg[3], empreg[4], empreg[5], ajuda_de_custo)
    salario_adm = adm.calcular_salario(adm.salario_base, adm.imposto, adm.ajuda_de_custo)
    print(adm.__repr__() + f'.\nDessa forma tem um salario total de {salario_adm}')

def main_vendedor(empreg) :

    valor_producao = int(input('Quanto produziu em euros o operario?'))
    comissao = float(input('Qual o valor da comissao que o operario ira ganhar? Esse valor é um float entre 0 e 1! '))

    """valor_vendas = 20000 #produziu 20 mil euros
    comissao = 0.1 # ganha 10% do valor produzido"""
    vend = Vendedor(empreg[0], empreg[1], empreg[2], empreg[3], empreg[4], empreg[5], valor_producao, comissao)
    print(vend.__repr__() + f'\nO salario base do {vend.nome} é de {vend.calcular_salario(vend.salario_base, vend.imposto, vend.valor_vendas, vend.comissao)}')

def main_operario(empreg) :

    valor_producao = int(input('Quanto produziu em euros o operario?'))
    comissao = float(input('Qual o valor da comissao que o operario ira ganhar? '))


    """ valor_producao = 20000 #produziu 20 mil euros
    comissao = 0.1 # ganha 10% do valor produzido"""
    oper = Operario(empreg[0], empreg[1], empreg[2], empreg[3], empreg[4], empreg[5], valor_producao, comissao)
    print(oper.__repr__() + f'\nO salario base do {oper.nome} é de {oper.calcular_salario(oper.salario_base, oper.imposto, oper.valor_producao, oper.comissao)}')

def main() :

    while True:
        opcoes = ['1', '2', '3', '4', '5', '0']
        a = input('''\n                                                             MENU
        ==========================================================================================================
        Deseja consultar qual opção:
                        
                        (1) Empregado     (2) Fornecedor     (3) Administrador     (4) Operario     (5)Vendedor
                        
                        Para sair digite (0)
                        
         ==========================================================================================================
          Opção> ''')
        if a not in opcoes:
            print('opcao invalida')
            continue
        else:
            pessoa = main_pessoa()
            if a == '1':
                empregado = main_empregado(pessoa)
                print(empregado[8][0], empregado[8][1])
            elif a == '2':

                main_fornecedor(pessoa)
            elif a == '3':
                empregado = main_empregado(pessoa)
                main_administrador(empregado)
            elif a == '4':
                empregado = main_empregado(pessoa)
                main_operario(empregado)
            elif a=='5':
                empregado = main_empregado(pessoa)
                main_vendedor(empregado)
            elif a == '0':
                break
            else:
                print('Does not match, Try Again')
                continue

main()
