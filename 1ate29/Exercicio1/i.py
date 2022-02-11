genero=input("Qual o seu genero:")
a = float(input("introduza a sua altura:"))
def peso():
    ph=(72.7*a)-58
    pm=(62.1*a)-44.7
    while True:
        if genero== "m":
            print("o seu peso é:", ph)
            break
        elif genero=="f":
            print("o seu peso é:", pm)
            break
        else:
            print("opção inválida")

peso()