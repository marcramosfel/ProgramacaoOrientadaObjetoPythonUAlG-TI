from math import *

def quadrado():
    lado=float(input("insira o valor do lado:"))
    area=lado * lado
    perimetro=lado**2 * pi

    print("O valor da área é:",area)
    print("O valor do perimetro é:" ,perimetro)

quadrado()