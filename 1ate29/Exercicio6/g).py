frase = str(input('Introduza uma frase:'))

def inversa(frase):
    if frase == frase[::-1]:
        print('palindromo\n', frase, frase[::-1])
    else:
        print('nao e palindromo')

inversa(frase)
