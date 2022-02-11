lista=list(range(1,101))

"""
def dez_primeiros(lista):
    print(lista[0:10])

dez_primeiros(lista)


def dez_ultimos(lista):
    print(lista[90:100])

dez_ultimos(lista)


def pos10_pos20(lista):
    print(lista[10:20])

pos10_pos20(lista)


def apaga_pos5(lista):
    del lista[5]

apaga_pos5(lista)
dez_primeiros(lista)

def apaga_numero(lista):
    lista.remove(20)
    print(lista)
    print('numero 20 apagado')

apaga_numero(lista)

def inversa(lista):
    print(lista[::-1])

inversa(lista)"""

def abc(lista):
    lista_abc = {'a', 'b', 'c'} #isto é um set, e tipo um dicionario mas sem values.
    """lista += lista_abc
    print(lista)
    """
    lista_abc=lista_abc.union(lista)
    print(lista_abc)#o parametro de entrada tem de ser um iteravel


    lista_abc2 = ['a', 'b', 'c', 'd']
    lista_abc.update(lista_abc2)
    print(lista_abc)
abc(lista)
