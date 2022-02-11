

def numeros():
    numeros = int(input("Quantos numeros: "))

    primeiro = int(input("Numero 1: "))
    count = 1
    maior = primeiro
    soma = primeiro
    while count < numeros:
        count += 1
        temp=int(input("Numero %d: " % count))
        soma += temp
        if temp>maior:
            maior = temp
    print(soma)
    print('o maior é:',maior)


numeros()