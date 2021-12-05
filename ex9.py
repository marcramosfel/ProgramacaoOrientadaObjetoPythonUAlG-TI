import os.path
import pickle

class Person:
    def __init__(self, forename, surname, address, cc, phone) :
        self.forename = forename
        self.surname = surname
        self.address = address
        self.cc = cc
        self.phone = phone

    def __repr__(self):
        return f'{self.forename}, {self.surname}, {self.address}, {self.cc}, {self.phone}'

    @property
    def forename(self):
       return self.__forename

    @forename.setter
    def forename(self, forename):
        self.__forename = forename

    @property
    def surname(self) :
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def address(self) :
        return self.__address

    @address.setter
    def address(self, address) :
        self.__address = address

    @property
    def cc(self) :
        return self.__cc

    @cc.setter
    def cc(self, cc) :
        self.__cc = cc

    @property
    def phone(self) :
        return self.__phone

    @phone.setter
    def phone(self, phone) :
        self.__phone = phone

class Carro:
    def __init__(self, brand, model, kms, comsuption, cor, dono, motor):
        self.brand = brand
        self.model = model
        self.kms = kms
        self.comsuption = comsuption
        self.cor = cor
        self.dono = dono
        self.motor = motor

    def __repr__(self):
        return f'{self.brand, self.model, self.kms, self.comsuption, self.cor, self.dono, self.motor}'


    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, motor):
        self.__motor = motor

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def kms(self):
        return self.__kms
    @kms.setter
    def kms(self, kms):
        self.__kms = kms

    @property
    def comsuption(self):
        return self.__comsuption
    @comsuption.setter
    def comsuption(self, comsuption):
        self.__comsuption = comsuption

class Engine:
    def __init__(self, fuel, horsepower, torque, displacement):
        self.fuel = fuel
        self.horsepower = horsepower
        self. torque = torque
        self.displacement = displacement

    def __repr__(self):
        return f'{self.fuel}, {self.horsepower}, {self.torque}, {self.displacement}'

    @property
    def fuel(self):
        return self.__fuel
    @fuel.setter
    def fuel(self, fuel):
        self.__fuel = fuel

    @property
    def horsepower(self):
        return self.__horsepower
    @horsepower.setter
    def horsepower(self, horsepower):
        self.__horsepower = horsepower

    @property
    def torque(self):
        return self.__torque
    @torque.setter
    def torque(self, torque):
        self.__torque = torque

    @property
    def displacement(self):
        return self.__displacement

    @displacement.setter
    def displacement(self, displacement):
        self.__displacement = displacement

class Cor:
    def __init__(self, nome, r, g, b):
        self.nome = nome
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f'{self.nome},[{self.r}, {self.g}, {self.b}]'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def r(self) :
        return self.__r

    @r.setter
    def r(self, r) :
        self.__r = r

    @property
    def g(self) :
        return self.__g

    @g.setter
    def g(self, g) :
        self.__g = g

    @property
    def b(self) :
        return self.__b

    @b.setter
    def b(self, b) :
        self.__b = b

class Lista:
    def __init__(self):
        self._stack = {}

    def adicionar(self, object):

        ancora = list(self._stack.keys())
        if ancora != []:
            # print(ancora)
            # so da pra usar com essa ancora "ultimo id", pois caso seja apagado o len(ancora) sera substituido
            # e nao incrementado, dessa forma o dicionario fica travado pelo ultimo id
            ultimo_id = ancora[len(ancora)-1]
            self._stack[ultimo_id + 1] = object
        else:
            self._stack[1] = object

    def editar(self):
        pass

    def apagar(self, id):
        #id é um string com os atributos referentes
        if self.is_empty():
            raise ValueError
        else:
            del self._stack[id]


    def is_empty(self):
        if len(self._stack) == 0:
            return True
        else:
            return False

    def len(self):
        return self._stack.__len__()

    def __repr__(self):
        """saida = ' '
        for elem in self._stack[::-1]:
            saida = str(elem) + ',' + saida
        saida = saida[:-2]
        #return '[' + saida + ']'"""
        return f"{self._stack}"

def editar_pessoas(lista_carros, lista_cores, lista_engine, lista_pessoas):

    for id, atributo  in lista_pessoas._stack.items():
        print("|", id, end = " |")
    print()
    id_pessoa = int(input('Qual id da pessoa quer editar> '))
    ancora = lista_pessoas._stack[id_pessoa]
    opcao = 1
    while opcao != "0":
        print(f"""Veja os atributos que pode editar:
            # Parar de editar> 0
            # Atuais> {lista_pessoas._stack[id_pessoa]}
            1 . Forename
            2 . Surname
            3 . CC
            4 . Phone""")
        opcao = input('Opcao> ')
        if opcao == "1":
            ancora.forename = input('Qual o novo nome? ')
        elif opcao == "2":
            ancora.surname =  input('Qual o novo apelido? ')
        elif opcao == "3":
            ancora.cc = input('Qual o novo CC? ')
        elif opcao == "4":
            ancora.phone = input('Qual o novo telefone? ')

def editar_carros(lista_carros, lista_cores, lista_engine, lista_pessoas):

    for id, atributo  in lista_carros._stack.items():
        print("|", id, end = " |")
    print()
    id_carros = int(input('Qual id da carros quer editar> '))
    ancora = lista_carros._stack[id_carros]
    opcao = 1
    while opcao != "0":
        print(f"""Veja os atributos que pode editar:
            # Parar de editar> 0
            # Atuais> {lista_carros._stack[id_carros]}
            1 . brand 
            2 . model 
            3 . kms 
            4 . comsuption 
            5 . cor 
            6 . dono 
            7 . motor""")
        opcao = input('Opcao> ')
        if opcao == "1":
            ancora.brand = input('Qual o novo nome? ')
        elif opcao == "2":
            ancora.model =  input('Qual o novo horsepower? ')
        elif opcao == "3":
            ancora.kms = input('Qual o novo torque? ')
        elif opcao == "4":
            ancora.comsuption = input('Qual o novo consuption? ')
        elif opcao == "5":
            print(lista_cores._stack)
            id_cor = int(input('Qual id da cor quer para o carro?'))
            ancora.cor = lista_cores._stack[id_cor]
        elif opcao == "6":
            print(lista_pessoas)
            id_pessoa = int(input('Qual o id da pessoa que será o dono do carro?'))
            ancora.dono = lista_pessoas._stack[id_pessoa]
        elif opcao == "7":
            print(lista_engine)
            id_engine = int(input('Qual id do motor quer para o carro?'))
            ancora.motor = lista_engine._stack[id_engine]

def editar_engine(lista_carros, lista_cores, lista_engine, lista_pessoas):

    for id, atributo  in lista_engine._stack.items():
        print("|", id, end = " |")
    print()
    id_engine = int(input('Qual id da engine quer editar> '))
    ancora = lista_engine._stack[id_engine]
    opcao = 1
    while opcao != "0":
        print(f"""Veja os atributos que pode editar:
            # Parar de editar> 0
            # Atuais> {lista_engine._stack[id_engine]}
            1 . Fuel
            2 . Horsepower
            3 . Torque
            4 . Displacement""")
        opcao = input('Opcao> ')
        if opcao == "1":
            ancora.fuel = input('Qual o novo nome? ')
        elif opcao == "2":
            ancora.horsepower =  input('Qual o novo horsepower? ')
        elif opcao == "3":
            ancora.torque = input('Qual o novo torque? ')
        elif opcao == "4":
            ancora.displacement = input('Qual o novo displacement? ')

def editar_cores(lista_carros, lista_cores, lista_engine, lista_pessoas):

    for id, atributo  in lista_cores._stack.items():
        print("|", id, end = " |")
    print()
    id_cores = int(input('Qual id da cores quer editar> '))
    ancora = lista_cores._stack[id_cores]
    opcao = 1
    while opcao != "0":
        print(f"""Veja os atributos que pode editar:
            # Parar de editar> 0
            # Atuais> {lista_cores._stack[id_cores]}
            1 . Nome
            2 . R
            3 . G
            4 . B""")
        opcao = input('Opcao> ')
        if opcao == "1":
            ancora.nome = input('Qual o novo nome? ')
        elif opcao == "2":
            ancora.r = input('Qual o novo r? ')
        elif opcao == "3":
            ancora.g = input('Qual o novo g? ')
        elif opcao == "4":
            ancora.b = input('Qual o novo b? ')

def inserir_carro(lista_carros, lista_cores, lista_engine, lista_pessoas):
    # validar se pode inserir carro (depende se existe lista de pessoas, motores, etc...
    if lista_cores.is_empty():
        print('''Não é possivel adiconar carro, pois nao existe nenhum cor criada. 
Crie uma cor ou verique se tem dados guardados referentes a cor e carregue-os primeiro!''')
    elif lista_engine.is_empty():
        print('''Não é possivel adiconar carro, pois nao existe nenhum motor criado. 
Crie um motor ou verique se tem dados guardados referentes ao motor e carregue-os primeiro!''')
    elif lista_pessoas.is_empty():
        print('''Não é possivel adiconar carro, pois nao existe nenhuma pessoa criada. 
Crie uma pessoa ou verique se tem dados guardados referentes a pessoa e carregue-as primeiro!''')
    else:
        print("A inserir atributos de carro")
        brand = input('brand?')
        model = input('model')
        kms = input('kms?')
        comsuption = int(input('comsuption'))

        """brand = "vw"
        model = "golf"
        kms = 12       #apenas para testes
        comsuption = 12"""

        print(lista_cores)
        id_cor = int(input('Qual id da cor quer para o carro?'))
        print(lista_engine)
        id_engine = int(input('Qual id do motor quer para o carro?'))
        print(lista_pessoas)
        id_pessoa = int(input('Qual o id da pessoa que será o dono do carro?'))
        carro = Carro(brand, model, kms, comsuption, lista_cores._stack[id_cor], lista_pessoas._stack[id_pessoa], lista_engine._stack[id_engine])
        lista_carros.adicionar(carro)
        print(lista_carros)

def inserir_pessoa(lista_carros, lista_cores, lista_engine, lista_pessoas):
    print("A inserir atributos de pessoa")

    forname = input("Forname?")
    surname = input("Surname?")
    address = input("Address?")
    cc = input("CC?")
    phone = input("Phone?")

    """forname = "marcos"
    surname = "ramos"
    address = "faro" #apenas para testes
    cc = "123"
    phone = 123"""

    pessoa = Person(forname, surname, address, cc, phone)
    lista_pessoas.adicionar(pessoa)
    print(lista_pessoas)

def inserir_engine(lista_carros, lista_cores, lista_engine, lista_pessoas):
    print("A inserir atributos de motor")

    fuel = input('fuel?')
    horsepower = input('horsepower?')
    torque = input('torque?')
    displacement = input('displacement?')

    """fuel = "gasolina"
    horsepower = 2        #apenas para testes
    torque = 1
    displacement = 23"""

    motor = Engine(fuel, horsepower, torque, displacement)
    lista_engine.adicionar(motor)
    print(lista_engine)

def inserir_cor(lista_carros, lista_cores, lista_engine, lista_pessoas):
    print("A inserir atributos de cor")
    nome = input('nome?')
    r = input('r?')
    g = input('g?')
    b = input('b?')

    """nome = "vermelho"
    r = 255                #apenas para testes
    g = 1
    b = 2"""

    cor = Cor(nome, r, g, b)
    lista_cores.adicionar(cor)
    print(lista_cores)

def listar_carros(lista_carros, lista_cores, lista_engine, lista_pessoas):
    print(lista_carros)

def listar_cores(lista_carros, lista_cores, lista_engine, lista_pessoas):
    print(lista_cores)

def listar_engines(lista_carros, lista_cores, lista_engine, lista_pessoas):
    print(lista_engine)

def listar_pessoas(lista_carros, lista_cores, lista_engine, lista_pessoas):
    print(lista_pessoas._stack)

def guardar_dados(lista_carros, lista_cores, lista_engine, lista_pessoas):

    if lista_pessoas._stack != {}:
        with open('lista_pessoa.pickle', "wb") as f:
            pickle.dump(lista_pessoas, f)

    if lista_cores._stack != {}:
        with open('lista_cores.pickle', "wb") as f:
            pickle.dump(lista_cores, f)

    if lista_engine._stack != {}:
        with open('lista_engine.pickle', "wb") as f:
            pickle.dump(lista_engine, f)

    if lista_carros._stack != {}:
        with open('lista_carro.pickle', "wb") as f:
            pickle.dump(lista_carros, f)

def apagar_pessoas(lista_carros, lista_cores, lista_engine, lista_pessoas):
    for pessoa, atributos in lista_pessoas._stack.items():
        print(pessoa, "=", atributos)
    idpessoa = int(input("Qual id da pessoa quer apagar? "))
    lista_pessoas.apagar(idpessoa)

def apagar_carros(lista_carros, lista_cores, lista_engine, lista_pessoas):
    for carro, atributos in lista_carros._stack.items():
        print(carro, "=", atributos)
    idcarro = int(input("Qual id da carro quer apagar? "))
    lista_carros.apagar(idcarro)

def apagar_engine(lista_carros, lista_cores, lista_engine, lista_pessoas):
    for engine, atributos in lista_engine._stack.items():
        print(engine, "=", atributos)
    idengine = int(input("Qual id da idengine quer apagar? "))
    lista_engine.apagar(idengine)

def apagar_cores(lista_carros, lista_cores, lista_engine, lista_pessoas):
    for cor, atributos in lista_cores._stack.items():
        print(cor, "=", atributos)
    idcor = int(input("Qual id da cor quer apagar"))
    lista_cores.apagar(idcor)

def menu (lista_carros, lista_cores, lista_engine, lista_pessoas):
    #lista_id = [11, 22, 33, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44,0]
    lista_id = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44, 50]
    funcoes = [inserir_carro, apagar_carros, listar_carros, editar_carros,
               inserir_pessoa, apagar_pessoas, listar_pessoas, editar_pessoas,
               inserir_engine, apagar_engine, listar_engines, editar_engine,
               inserir_cor, apagar_cores, listar_cores, editar_cores,
               guardar_dados]

    opcoes = {chave: valor for (chave, valor) in zip(lista_id, funcoes)}

    opcao = 1
    while (opcao != 0):
        print("""
        _________________________________________________
        |                    MENU                       |
        |_______________________________________________|
        |11. Inserir Carro    |    21. Inserir Pessoa   |
        |12. Apagar Carro     |    22. Apagar Pessoa    |
        |13. Listar Carro     |    23. Listar Pessoa    |
        |14. Editar Carro     |    24. Editar Pessoa    |
        |_____________________|_________________________|
        |31. Inserir Motor    |    41. Inserir cor      |
        |32. Apagar Motor     |    42. Apagar cor       |
        |33. Listar Motor     |    43. Listar cor       |  
        |34. Editar Motor     |    44. Editar cor       | 
        |_____________________|_________________________| 
        |0. Sair              |    50-Guardar           |
        |_____________________|_________________________|
        """)

        opcao = int(input("Opção: "))
        if (opcao in opcoes.keys()):
            opcoes[opcao](lista_carros, lista_cores, lista_engine, lista_pessoas)


if __name__ == "__main__":
    #VER se existe ficheiro com dados, logo carregar
    #neste caso carrega sempre caso o arquivo exista
    #caso queira testar sem dados, remover os ficheiros pickles ou tira-los da pasta

    if os.path.isfile('lista_pessoa.pickle'):
        print('tem o arquivo pessoas, sera carregado pessoas')
        with open('lista_pessoa.pickle', 'rb') as f:
            lista_pessoas = Lista()
            loader = pickle.load(f)
            """print(type(loader))
            print(loader,type(loader._stack))"""
            lista_pessoas._stack = loader._stack #subscreve em stack de pessoas o loader referente, o mesmo se sucede para as classe em baixo
            print(lista_pessoas)
    else:
        lista_pessoas = Lista()

    if os.path.isfile('lista_carro.pickle'):
        print('tem o arquivo carros, sera carregado carros')
        with open('lista_carro.pickle', 'rb') as f:
            lista_carros = Lista()
            loader = pickle.load(f)
            lista_carros._stack = loader._stack
            print(lista_carros)
    else:
        lista_carros = Lista()

    if os.path.isfile('lista_engine.pickle'):
        print('tem o arquivo enigine, sera carregado engine')
        with open('lista_engine.pickle', 'rb') as f:
            lista_engine = Lista()
            loader = pickle.load(f)
            lista_engine._stack = loader._stack
            print(lista_engine)
    else:
        lista_engine = Lista()

    if os.path.isfile('lista_cores.pickle'):
        print('tem o arquivo cores, sera carregado cores')
        with open('lista_cores.pickle', 'rb') as f:
            lista_cores = Lista()
            loader = pickle.load(f)
            lista_cores._stack = loader._stack
            print(lista_cores)
    else:
        lista_cores = Lista()





    menu(lista_carros, lista_cores, lista_engine, lista_pessoas)
