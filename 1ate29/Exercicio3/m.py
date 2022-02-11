a = int(input("Digite o valor de n: "))
def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    print("O valor de %d! eh =" %n, fat)


fatorial(a)