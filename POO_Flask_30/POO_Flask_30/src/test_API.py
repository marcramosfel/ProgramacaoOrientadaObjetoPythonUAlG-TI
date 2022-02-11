import requests

uri = 'http://localhost:5000/reading'
####GETALLL####
print(20 * '*' + ' GET all ' + 20 * '*')
response = requests.get(uri)
print(response.text)
input('\nPress enter to continue...\n')
####GETONE####
print(20 * '*' + ' GET one ' + 20 * '*' )
response = requests.get(uri + '/1')
print(response.text)
input('\nPress enter to continue...\n')
####POST####
print(20 * '*' + ' POST ' + 20 * '*')
response = requests.post(uri, json={
      'idReading': 'DEFAULT',
      'idSensor': 1,
      'timestamp': 'DEFAULT',
      'value': 1021
    })
print(response.text)
input('\nPress enter to continue...\n')
####PUT####
print(20 * '*' + ' PUT ' + 20 * '*')
response = requests.put(uri + '/2', json={
      'value': '716',
    })
print(response.text)
input('\nPress enter to continue...\n')
####GETALLL####
print(20 * '*' + ' GET all (again) ' + 20 * '*')
response = requests.get(uri)
print(response.text)
input('\nPress enter to continue...\n')
####DELETE####
print(20 * '*' + ' DELETE ' + 20 * '*')
response = requests.get(uri).json()
id = response['readings'][0]['idReading']
response = requests.delete(uri + f'/{id}')
print(response.text)
input('\nPress enter to continue...\n')
####GETALLL####
print(20 * '*' + ' GET all (again) ' + 20 * '*')
response = requests.get(uri)
print(response.text)
print('Test realizado com sucesso!')
