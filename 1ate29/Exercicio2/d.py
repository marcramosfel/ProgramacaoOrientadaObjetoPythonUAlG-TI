while True:
    letra=input("introduza uma letra:")
    if not letra.isdigit() and len(letra)==1:
        break
    else:
        print("não é possível adicionar numeros ou mais do que uma letra")
#if letra == "a" or letra == "e" or letra == "i" or letra== "u" or letra == "o":
if letra in ('a', 'e', 'i', 'o', 'u'):
    print("É vogal")
else:
    print("É consoante")