import mysql.connector

'''Comece por restaurar a base de dados Adamastor num servidor MySQL. Observe a
Figura 4 que apresenta o diagrama de entidade relacionamento da referida base de dados.
Usando uma conexão Python crie uma classe com um método que responde/faz o necessário
para responder às seguintes questões/pedidos (veja exemplo na Figura 5 – ver bitbucket para
ter código fonte):

(i) apresente uma listagem de produtos ordenados pelo preço unitário.    ✔

(ii) apresente uma listagem de produtos com stock inferior a 10 unidades.   ✔

(v) apresente uma listagem de produtos com menos de 10 unidades em stock e sem encomendas. ✔

(ix) apresente uma listagem de produtos com os respetivos fornecedores. ✔

(xii) apresente uma listagem das datas das encomendas efetuadas por “Hanari Carnes”. ✔

(xiv) apresente uma listagem dos empregados que trataram de encomendas feitas por “Hanari Carnes”. ✔

(xx) Alterar o número de unidades em stock para as existentes mais as encomendadas nos
produtos do fornecedor com id 1 e colocar as encomendadas feitas a este a 0. ✔

(xxiv) Inserir um novo funcionário (invente os dados necessários). ✔

(xxxi) Quais as cidades que têm fornecedores (devolver o resultado todos em maiúsculas)? ✔

(xxxiv) Qual a maior encomenda em termos de valor? ✔

(xxxv) Qual a maior encomenda em termos de número de itens? ✔    '''

config = {
    'host': 'localhost',
    'user': 'root',
    'db': 'adamastor'

}


class Adamastor:
    def __init__(self):
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor(dictionary=True)

    def atualiza_existencia(self):
        sql = """UPDATE produtos 
                 SET 
                    Existências = (Existências + UnidadesEncomendadas),
                    UnidadesEncomendadas = 0
                 WHERE
                    (CódigoDoFornecedor = 1)
              """
        self.cursor.execute(sql)
        self.cnx.commit()
        print('Atualizado')

    def insere_empregado(self):
        sql = """ INSERT  INTO  empregados (
                        CódigoDoEmpregado, 
                        Apelido, 
                        Nome, 
                        Cargo,
                        TítuloDeCortesia,
                        DataDeNascimento,
                        DataDeContratação,
                        Endereço,
                        Cidade,
                        Região,
                        CódigoPostal,
                        País,
                        Telefone,
                        Extensão,
                        Fotografia,
                        Notas,
                        Superior
                        
                    ) VALUES (
                        DEFAULT, 
                        %(Apelido)s, 
                        %(Nome)s,
                        %(Cargo)s,
                        %(TítuloDeCortesia)s,
                        %(DataDeNascimento)s,
                        %(DataDeContratação)s,
                        %(Endereço)s,
                        %(Cidade)s,
                        %(Região)s,
                        %(CódigoPostal)s,
                        %(País)s,
                        %(Telefone)s,
                        %(Extensão)s,
                        %(Fotografia)s,
                        %(Notas)s,
                        %(Superior)s
                        
                    )
            """

        data = dict()
        for atributo in (
        "Apelido", "Nome", "Cargo", "TítuloDeCortesia", "DataDeNascimento", "DataDeContratação", "Endereço",
        "Cidade", "Região", "CódigoPostal", "País", "Telefone", "Extensão", "Fotografia", "Notas", "Superior"):
            data[atributo] = input(f"{atributo}? ")

        self.cursor.execute(sql, data)
        # print(sql)
        self.cnx.commit()
        print('Empregado adicionado')

    '''def listar_clientes(self) :
        sql = 'select * from clientes'
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for clientes in myresult:
            print (clientes)

    def listar_clientes_da_cidade(self, cidade) :
        sql = 'select * from clientes where cidade = %s'
        self.cursor.execute(sql, (cidade,))
        myresult = self.cursor.fetchall()
        for clientes in myresult:
            print(clientes)'''

    def listar_produtos(self):
        sql = 'select NomeDoProduto, PreçoUnitário from produtos order by PreçoUnitário'
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for produto in myresult:
            print(produto)

    def empregados_trataram_encomendas_de_hanar(self):
        sql = '''SELECT 
                    encomendas.CódigoDoCliente,
                    encomendas.CódigoDoEmpregado,
                    empregados.Nome
                FROM
                    encomendas
                        INNER JOIN
                    empregados ON encomendas.CódigoDoEmpregado = empregados.CódigoDoEmpregado
                WHERE
                    CódigoDoCliente = 'HANAR'
                group by CódigoDoEmpregado'''
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for produto in myresult:
            print(produto)

    def listar_stock_menor_que_10(self):
        sql = 'SELECT NomeDoProduto, Existências FROM produtos WHERE Existências < 10 ORDER BY Existências'
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for produto in myresult:
            print(produto)

    def listar_stock_menor_que_10_sem_encomendas(self):
        sql = 'SELECT * FROM adamastor.produtos where Existências < 10 and UnidadesEncomendadas = 0'
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for produto in myresult:
            print(produto)

    def listar_produtos_respetivos_fornecedores(self):
        sql = 'SELECT produtos.NomeDoProduto, fornecedores.NomeDaEmpresa, fornecedores.CódigoDoFornecedor ' \
              'FROM fornecedores INNER JOIN produtos ON produtos.CódigoDoFornecedor = fornecedores.CódigoDoFornecedor ' \
              'ORDER BY produtos.CódigoDoFornecedor'
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for produto in myresult:
            print(produto)

    def data_encomenda_hanar(self):
        sql = "SELECT CódigoDoCliente, DataDaEncomenda FROM encomendas WHERE CódigoDoCliente = 'HANAR'"
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for data in myresult:
            print(data)

    def listar_cidades_fornecedores(self):
        sql = "SELECT UPPER(fornecedores.Cidade) AS Cidade, UPPER(fornecedores.NomeDaEmpresa) AS Empresa from fornecedores " \
              "ORDER BY fornecedores.Cidade"
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for cidades in myresult:
            print(cidades, "\n")

    def maior_emcomenda(self):
        sql = """SELECT 
                    CódigoDaEncomenda, SUM(Quantidade) AS total
                FROM
                    adamastor.detalhes_da_encomenda
                GROUP BY CódigoDaEncomenda
                ORDER BY total DESC
                LIMIT 1"""
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for items in myresult:
            print(items, "\n")

    def maior_emcomenda_valor(self):
        sql = """SELECT 
                    CódigoDaEncomenda, SUM(PreçoUnitário * Quantidade) AS total
                FROM
                    adamastor.detalhes_da_encomenda
                GROUP BY CódigoDaEncomenda
                ORDER BY total DESC
                LIMIT 1"""
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for valor in myresult:
            print(valor, "\n")


def main():
    adam = Adamastor()
    while True:
        print(160 * '#')
        print()
        a = input('''   
                        ______________________________________________________________________________________________________________________
                        |                            Digite qual opção quer realizar na base de dados Adamastor:                             |
                        |____________________________________________________________________________________________________________________|    
                        |(1) |                      Apresente uma listagem de produtos ordenados pelo preço unitário. ✔                      |
                        |____|_______________________________________________________________________________________________________________|
                        |(2) |                     Apresente uma listagem de produtos com stock inferior a 10 unidades. ✔                    |
                        |____|_______________________________________________________________________________________________________________|
                        |(5) |            Apresente uma listagem de produtos com menos de 10 unidades em stock e sem encomendas. ✔           |
                        |____|_______________________________________________________________________________________________________________|
                        |(9) |                       Apresente uma listagem de produtos com os respetivos fornecedores. ✔                    |
                        |____|_______________________________________________________________________________________________________________|
                        |(12)|               Apresente uma listagem das datas das encomendas efetuadas por “Hanari Carnes”. ✔                |
                        |____|_______________________________________________________________________________________________________________|
                        |(14)|         Apresente uma listagem dos empregados que trataram de encomendas feitas por “Hanari Carnes”. ✔        |
                        |____|_______________________________________________________________________________________________________________|
                        |(31)|               Quais as cidades que têm fornecedores (devolver o resultado todos em maiúsculas)? ✔             |
                        |____|_______________________________________________________________________________________________________________|
                        |    |  Alterar o número de unidades em stock para as existentes mais as encomendadas nos produtos do fornecedor     |
                        |(20)|                             com id 1 e colocar as encomendadas feitas a este a 0.                             |
                        |____|_______________________________________________________________________________________________________________|
                        |(24)|                           Inserir um novo funcionário (invente os dados necessários). ✔                       |
                        |____|_______________________________________________________________________________________________________________|
                        |(34)|                                   Qual a maior encomenda em termos de valor? ✔                                |
                        |____|_______________________________________________________________________________________________________________|
                        |(35)|                             Qual a maior encomenda em termos de número de itens? ✔                            |
                        |____|_______________________________________________________________________________________________________________|
                        |(0) |                                                 SAIR                                                          |
                        |____|_______________________________________________________________________________________________________________|
            
            Opção> ''')

        if a == '1':
            adam.listar_produtos()

        elif a == '2':
            adam.listar_stock_menor_que_10()

        elif a == '5':
            adam.listar_stock_menor_que_10_sem_encomendas()

        elif a == '9':
            adam.listar_produtos_respetivos_fornecedores()

        elif a == '12':
            adam.data_encomenda_hanar()

        elif a == '14':
            adam.empregados_trataram_encomendas_de_hanar()

        elif a == '20':
            adam.atualiza_existencia()

        elif a == '24':
            adam.insere_empregado()

        elif a == '31':
            adam.listar_cidades_fornecedores()

        elif a == '34':
            adam.maior_emcomenda_valor()

        elif a == '35':
            adam.maior_emcomenda()

        elif a == '0':
            break

        else:
            print('Opçaõ Invalida')
            continue

main()
