import requests
from tabulate import tabulate

uri = 'http://localhost:5000/reading'

def get_all():
    print(20 * '*' + ' GET all ' + 20 * '*')
    response = requests.get(uri)
    #print(response.text)
    print(response.json()['message'])
    #print(response.json()['readings'])

    dicionario_readings = response.json()['readings']
    lista_tabulate = []

    for i in range(len(dicionario_readings)):
        for value in dicionario_readings[i].values():
            lista_tabulate.append(value)

    lista_bidemensional = [[['']]*4 for i in zip(range(len(lista_tabulate)//4))]

    for k in range(len(lista_tabulate)//4):
        for l in range(4):
            lista_bidemensional[k][l] = lista_tabulate[l+k*(4)]


    #print(lista_tabulate)
    #print(lista_bidemensional)
    print(tabulate(lista_bidemensional, headers=['idReading', 'idSensor', 'timestamp', 'value'], tablefmt='psql'))

def get_one():
    print(20 * '*' + ' GET one ' + 20 * '*')

    id = input('Qual id gostaria de realizar a consulta?')
    response = requests.get(uri + f'/{id}').json()

    print(response["message"])
    dicionario_readings = response['readings']
    lista_tabulate = []


    for value in dicionario_readings.values():
        lista_tabulate.append(value)

    lista_bidimensional = [lista_tabulate]
    #print(lista_tabulate)
    print(tabulate(lista_bidimensional, headers=['idReading', 'idSensor', 'timestamp', 'value'], tablefmt='psql'))


def post():
    print(20 * '*' + ' POST ' + 20 * '*')
    idSensor = input('Qual id do sensor será utilizado?')
    value = input('Qual o valor tera o value nesse reading?')
    response = requests.post(uri, json={
        'idReading': 'DEFAULT',
        'idSensor': f'{idSensor}',
        'timestamp': 'DEFAULT',
        'value': f'{value}'
    }).json()
    print(response['message'])

def delete():
    print(20 * '*' + ' DELETE ' + 20 * '*')
    idReading = input('Qual registo quer apagar?')
    response = requests.delete(uri + f'/{idReading}').json()
    print(response['message'])
    #print(response.text)

def put():
    print(20 * '*' + ' PUT ' + 20 * '*')
    idReading = input('Qual o registo quer alterar?')
    value = input('Quaer alterar o value para quanto?')
    response = requests.put(uri + f'/{idReading}', json={
        'value': f'{value}',
    }).json()
    print(response['message'])

def menu():
    funcoes = [get_all, get_one, delete, put, post]
    ids = [1, 2, 3, 4, 5]
    opcoes = {chave: valor for (chave, valor) in zip(ids, funcoes)}
    opcao = 10
    while opcao != 0:
        print("""##################################################################################################
        _________________________________________________
        |                    MENU                       |
        |_______________________________________________|
        |    1. GET ALL       |    2. GET ONE           |
        |_____________________|_________________________|
        |    3. DELETE        |    4. PUT               |
        |_____________________|_________________________| 
        |    5. POST          |    0. Sair              |
        |_____________________|_________________________|   """)

        try:
            opcao = int(input('\nQual consulta quer realizar?'))
        except ValueError as err:
            print(err)
            continue
        if opcao in opcoes.keys():
            opcoes[opcao]()
        elif opcao == 0:
            print('Saindo...')
        else:
            print('Essa opção não é válida!')

if __name__ == '__main__':
    menu()