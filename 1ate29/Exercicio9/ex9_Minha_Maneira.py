import pickle

class Cor:
    def __init__(self, nome, r, g, b) :
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

    @classmethod
    def pergunta_cor(cls) :
        nome = input('nome?')
        r = input('r?')
        g = input('g?')
        b = input('b?')
        return cls(nome, r, g, b)

class Pessoa:
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
    def surname(self, surname) :
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

    @classmethod
    def pergunta_pessoa(cls):
        forename = input('forename?')
        surname = input('surname?')
        address = input('address?')
        cc = input('cc?')
        phone = input('phone?')
        return cls(forename, surname, address, cc, phone)

class Motor:
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

    @classmethod
    def pergunta_motor(cls):
        fuel = input('fuel?')
        horsepower = input('horsepower?')
        torque = input('torque?')
        displacement = input('displacement?')
        return cls(fuel, horsepower, torque, displacement)

class Carro:
    def __init__(self, brand, model, kms, comsuption):
                 #cor, pessoa, motor):
        self.brand = brand
        self.model = model
        self.kms = kms
        self.comsuption = comsuption
        #self.cor = cor
        #self.pessoa = pessoa
        #self.motor = motor

    def __repr__(self):
        return f'{self.brand, self.model, self.kms, self.comsuption}'
        #self.cor, self.motor, self.pessoa}'

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

    @staticmethod
    def car_owner(listacarros):
        for i in range(len(listacarros)):
            print(i, listacarros[i][0])
        carro = int(input('Qual o carro quer saber o proprietario?'))
        return f"\n{listacarros[carro][3]}"



    @classmethod
    def pergunta_carro(cls, lista_cores, lista_motores, lista_pessoas):
        brand = input('brand?')
        model = input('model')
        kms = input('kms?')
        comsuption = input('comsuption')
        print(list(zip(range(len(lista_cores)), lista_cores)))
        z = int(input('qual id da cor quer?'))
        print(list(zip(range(len(lista_motores)), lista_motores)))
        w = int(input('qual id do motor quer?'))
        print(list(zip(range(len(lista_pessoas)), lista_pessoas)))
        p = int(input('qual id da pessoa quer?'))

        return cls(brand, model, kms, comsuption), lista_cores[z], lista_motores[w], lista_pessoas[p]

def main() :
    lista_cores = []
    lista_carros = []
    lista_motores = []
    lista_pessoas = []

    while True :
        print("""
                                        MENU
                ______________________________________________________
                111 ver o dono do carro             
                11 lista carros                     21 lista pessoas
                12 novo carro                       22 nova pessoa
                13 apaga carro                      23 apaga pessoa

                31 lista cores                      41 lista motores
                32 nova cor                         42 novo motor
                33 apaga cor                        43 apaga motor

                g - guarda            c - carrega               0 - sai
                =======================================================

            """)
        op = input("opcao?\n")

        if op == '11':
            print(list(zip(
                range(len(lista_carros)), lista_carros)
            )
            )

        elif op == "111":
            print(Carro.car_owner(lista_carros))
        elif op == '12':
            lista_carros.append(Carro.pergunta_carro(lista_cores, lista_motores, lista_pessoas))

        elif op == '13' :
            idx = int(input("id da carro a apagar?"))
            del lista_carros[idx]

        elif op == '21' :
            print(list(zip(
                range(len(lista_pessoas)), lista_pessoas)
            )
            )
        elif op == '22' :
            lista_pessoas.append(Pessoa.pergunta_pessoa())

        elif op == '23' :
            idy = int(input("id da pessoa a apagar?"))
            del lista_cores[idy]

        elif op == '31' :
            print(
                list(zip(
                    range(len(lista_cores)), lista_cores)
                )
            )
        elif op == '32' :
            lista_cores.append(Cor.pergunta_cor())

        elif op == '33' :
            idz = int(input("id da cor a apagar?"))
            del lista_cores[idz]

        elif op == '41' :
            print(
                list(zip(
                    range(len(lista_motores)), lista_motores)
                )
            )
        elif op == '42' :
            lista_motores.append(Motor.pergunta_motor())

        elif op == '43' :
            idw = int(input("id do motor a apagar?"))
            del lista_cores[idw]


        elif op == 'g':
            with open('lista_todos.pickle', "wb") as f:
                pickle.dump(lista_cores, f)
                pickle.dump(lista_pessoas, f)
                pickle.dump(lista_motores, f)
                pickle.dump(lista_carros, f)

        elif op == 'c':
            with open('lista_todos.pickle', 'rb') as f:
                lista_cores = pickle.load(f)
                lista_pessoas = pickle.load(f)
                lista_motores = pickle.load(f)
                lista_carros = pickle.load(f)

        elif op == '0':
            break

main()