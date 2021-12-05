def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return f' {n}%3 = {n % 3}|\n {n}%5 = {n % 5}| \n>FizzBuzz<\n#########################################'

    elif n % 3 == 0:
        return f' {n}%3 = {n % 3}|\n {n}%5 = {n % 5}| \n>Fizz<\n#########################################'

    elif n % 5 == 0:
        return f' {n}%3 = {n % 3}|\n {n}%5 = {n % 5}| \n>Buzz<\n#########################################'

    else:
        return f' {n}%3 = {n % 3}|\n {n}%5 = {n % 5}| \n>{n}<\n#########################################'


def teste():
    for i in range(0, 100):
        print(fizzbuzz(i))


teste()
