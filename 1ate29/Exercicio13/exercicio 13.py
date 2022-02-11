
class Retangulo:
    __N = 0


    def __init__(self,lado):
        self.__lado = lado
        Retangulo.__N += 1

    @property
    def lado1(self):
        return self.__lado1

    @lado1.setter
    def lado1(self,lado1):
        self.__lado1 = lado1

    @property
    def lado2(self,lado2):
        return self.__lado2

    @lado2.setter
    def lado2(self,lado2):
        self.__lado2 = lado2


    def calcular_area(self):
        return self.__lado1*self.__lado2

    def calcular_perimetro(self):
        return self.__lado1*2 + self.__lado2*2

    def imprimir(self):
        print(f"Retangulo de lado {self.lado} tem área {self.calcular_perimetro()} e perimetro  {self.calcular_perimetro()}")

    def __repr__(self):
        return f"Retangulo de lado {self.lado} tem área {self.calcular_area()} e de periemtro {self.calcular_perimetro()} "


def menu_retangulo():

    lista_id = [1, 2, 3]
    objetos = [calcula_area, calcula_perimetro, conta_instancias]
    opcoes = {chave: valor for (chave, valor) in zip(lista_id, objetos)}

    opcao = 1
    while (opcao != 0):
        print("1. Calculo de área de retangulo")
        print("2. Calculo de perimetro de retangulo")
        print("3. Indica numero de instâncias/vezes que foram executadas operações")
        print("0. Sair")
        opcao = int(input("Opção: "))
        if (opcao in opcoes.keys()):
            opcoes[opcao]()

def calcula_area():
    lado = int(input("indique lado:"))
    print(Retangulo(lado).calcular_area())

def calcula_perimetro():
    lado = int(input("indique lado:"))
    print(Retangulo(lado).calcular_perimetro())

def conta_instancias():
    print(f'Numero de instancias: {Retangulo._conta_instancias()}')

    menu_retangulo()


class Quadrado:
    __N = 0

    def __init__(self, lado):
        self.__lado = lado
        Quadrado.__N += 1

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, lado):
        self.__lado = lado

    def calcular_area(self):
        return self.__lado*self.__lado

    def calcular_perimetro(self):
        return self.__lado*4

    def imprimir(self):
        print(f'Quadrado de lado {self.lado} tem área {self.calcular_area()} e perímetro {self.calcular_perimetro()}')

    def __repr__(self):
        return f'Quadrado de lado {self.lado} tem área {self.calcular_area()} e perímetro {self.calcular_perimetro()}'

    #completar com os restantes classes retangulo e circulo

    @classmethod
    def _conta_instancias(cls):
        return cls.__N

    @staticmethod
    def calcula_perimetro(lado):
        return lado * 4


def menu_quadrado():

    lista_id = [1, 2, 3]
    objetos = [calcula_area, calcula_perimetro, conta_instancias]
    opcoes = {chave: valor for (chave, valor) in zip(lista_id, objetos)}

    opcao = 1
    while (opcao != 0):
        print("1. Calculo de área de quadrado")
        print("2. Calculo de perimetro de quadrado")
        print("3. Indica numero de instâncias/vezes que foram executadas operações")
        print("0. Sair")
        opcao = int(input("Opção: "))
        if (opcao in opcoes.keys()):
            opcoes[opcao]()

def calcula_area():
    lado = int(input("indique lado:"))
    print(Quadrado(lado).calcular_area())

def calcula_perimetro():
    lado = int(input("indique lado:"))
    print(Quadrado(lado).calcular_perimetro())

def conta_instancias():
    print(f'Numero de instancias: {Quadrado._conta_instancias()}')

    menu_quadrado()


class menu_principal:



    def menu_principal():
        while True:
            print("1.Quadrado")
            opcao=int(input("introduza a sua opcao:"))

            if opcao== "1":
                menu_quadrado()
            else:
                print("opcao invalida")

    menu_principal()



