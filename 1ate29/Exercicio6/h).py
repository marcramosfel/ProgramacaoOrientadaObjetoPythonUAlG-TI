def escrever_extenso(numero):
    lista_ate_20 = ['um', 'dois', 'tres', 'quatro', 'cinque', 'seis', 'sete', 'oito', 'nove', 'dez',
                   'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezasseis', 'dezessete', 'dezoito', 'dezanove']

    lista_ate_cem = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem']

    lista_ate_mil = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos',
                     'setecentos', 'oitocentos', 'novecentos', 'mil']

    #print(numero%10, numero//10, (numero//10)%10)
    #print(numero%100, numero//100)
    #print(numero%10)

    for i in range(len(lista_ate_20)):
        if numero-1 == i:
            print(lista_ate_20[numero-1])
    if numero == 0:
        print('zero')
    elif 100 >= numero > 19:
        if numero == 100:
            print(lista_ate_cem[(numero//10) - 2])
        else:
            resto = numero % 10
            if resto == 0:
                print(lista_ate_cem[(numero//10) - 2])
            else:
                print(lista_ate_cem[(numero // 10) - 2], 'e' , lista_ate_20[resto-1])
    elif 100 < numero <= 1000:
        if numero == 1000:
            print(lista_ate_mil[(1000//100) - 1])
        else:
            centenas = (numero - numero % 100)//100
            dezenas = (numero//10) % 10
            if (numero // 10) % 10 != 0 and (numero // 10) % 10 != 1 and numero % 10 != 0:
                print(lista_ate_mil[centenas-1], 'e', lista_ate_cem[dezenas-2], 'e', lista_ate_20[(numero%10)-1])
            elif numero % 10 == 0:
                print(lista_ate_mil[centenas-1], 'e', lista_ate_cem[dezenas-2])
            else:
                print(lista_ate_mil[centenas-1], 'e', lista_ate_20[(numero % 100)-1])

    elif numero > 1000:
        print('Nao está preparado para números maiores que mil: 1000')


"""numero = 90.99

escrever_extenso(int(numero))
print('euros e')
escrever_extenso(round(((numero - ((numero*100)//100))*100)))
print('centimos')"""

try:
    for i in range(0, 1002):
        print(i, end=' = ')
        escrever_extenso(i)
    #escrever_extenso('str')
except Exception as err:
    print('Insira um numero entre 0 e 1000\n', err)