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

def menu():

    lista_id = [1, 2, 3, 4]
    objetos = [calcula_area, calcula_perimetro, conta_instancias, representacao]
    opcoes = {chave: valor for (chave, valor) in zip(lista_id, objetos)}
    print(opcoes)

    opcao = 1
    while (opcao != 0):
        print("1. Calculo de área de quadrado")
        print("2. Calculo de perimetro de quadrado")
        print("3. Indica numero de instâncias/vezes que foram executadas operações")
        print("4. Idica perimetro e área do quadrado")
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

def representacao():
    lado = int(input("indique lado:"))
    print(Quadrado(lado).__repr__())


if __name__ == "__main__":

    menu()