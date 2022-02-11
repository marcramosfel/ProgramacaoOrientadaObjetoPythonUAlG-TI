def tabuada(num: int):
    if (num < 0 or num >10):
        print("o numero é invalido")
        exit()
    for i in range(1, 11):
        yield str(num) + " x " + str(i) + " = " +str(num*i)

num = int(input("insira um numeor entre 1 e 10"))
resultado = tabuada(num)
for i in resultado:
    print(i)