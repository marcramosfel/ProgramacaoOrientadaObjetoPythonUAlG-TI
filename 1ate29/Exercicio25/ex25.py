class Data:
    def __init__(self, dia, mes, ano):
        """if Data.valida_data(dia, mes, ano):  # so atribui os objetos se todos eles passarem pela validacao
            self.ano, self.mes, self.dia = ano, mes, dia """# so atribui os objetos se todos eles passarem pela validacao
        self.ano, self.mes, self.dia = ano, mes, dia

    def __repr__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


    @staticmethod
    def valida_data(dia, mes, ano):
        ''' devolve True se a data e a/m/d valida . False caso contrario .
        : raises :
        TypeError : xxxxxxxx
        InvalidData : xxx excecao a ser implementada pelo aluno xxxx
            '''

        meses = [1,2,3,4,5,6,7,8,9,10,11,12]
        try:
            if ano <= int(0): # nao pode ser igual a zero
                raise Exception(ano, 'ano tem de ser maior que 0')

            if mes not in meses and mes < 0:
                raise Exception(mes, 'mes invalido pois nao pode ser negativo')
            elif mes not in meses and mes == 0:
                raise Exception(mes, 'mes invalido pois nao pode ser zero, tem de estar entre 1 e 12')
            elif mes not in meses:
                raise Exception(mes, 'mes invalido pois nao pode ser maior que 12')

            # Meses com 31 dias
            elif (mes == meses[0] or mes == meses[2] or mes == meses[4] or mes == meses[6]
                    or mes == meses[7] or mes == meses[9] or mes == meses[11]):
                if dia > 31 :
                    raise Exception(dia, 'dia invalido, como o mes é', mes, 'o dia deveria estar entre 1 e 31')
                elif dia < 0:
                    raise Exception(dia, 'dia invalido pois dia nao pode ser negativo')
                elif dia == 0:
                    raise Exception(dia, 'dia invalido pois dia nao pode ser zero.')

            # Meses com 30 dias
            elif mes == meses[3] or mes == meses[5] or mes == meses[8] or mes == meses[10]:
                if (dia > 30 ):
                    raise Exception(dia, 'dia invalido como mes é', mes, 'o dia deveria estar entre 1 e 30')
                elif dia < 0:
                    raise Exception(dia, 'dia dia invalido pois dia nao pode ser negativo')
                elif dia == 0:
                    raise Exception(dia, 'dia dia invalido pois dia nao pode ser zero.')

            elif meses[1]:
                # Testa se é bissexto
                if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                    if dia > 29 :
                        raise Exception(dia, 'dia invalido pois os dias em fevereiro, em ano bissexto so vão ate ao dia 29')
                    elif dia < 0:
                        raise Exception(dia, 'dia invalido pois dia nao pode ser negativo')
                    elif dia == 0:
                        raise Exception(dia, 'dia invalido pois dia nao pode ser zero.')
                elif dia > 28:
                    raise Exception(dia, 'dia invalido pois os dias em fevereiro, em ano normal so vão ate o dia 28')
                elif dia < 0:
                    raise Exception(dia, 'dia invalido pois dia nao pode ser negativo')
                elif dia == 0:
                    raise Exception(dia, 'dia invalido pois dia nao pode ser zero.')


            return True

        except Exception as validacoes:
            print(validacoes)
            return False

while True:
    verificar = input('Verificar Datas? S/N ').upper()
    if verificar =='S':
        pass
    elif verificar == 'N':
        break
    else:
        print('opcao nao valida')
        continue
    try:
        data = [int(input('Dia> ')), int(input('Mes> ')), int(input('Ano> '))]
        #print(Data.valida_data(data[0], data[1], data[2]))
        if Data.valida_data(data[0], data[1], data[2]):
            data = Data(data[0], data[1], data[2])   #so instancia caso seja verdadeiro
            print('data valida', data)
        else:
            print('data invalida') #nao e necessario fazer print pois caso entre no else significa que foi retornado falso,
            #e se foi retornado false entrou no else da funcao valida que ja faz o print da excecao


        print(80*"#")

    except ValueError as err:
        print(err)
