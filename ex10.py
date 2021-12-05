class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = []
        for i in range (3):
            if not isinstance(notas[i], float):
                raise
            else:
                self.notas.append(notas[i])
        self.media()

    def media(self):
        r = 0
        for i in range(len(self.notas)):
            r += self.notas[i]
        self.valor_media = r/3

    def __repr__(self):
        if self.valor_media<8:
            return f'Aluno {self.nome} reprovado pois {self.valor_media}'

        else:
            if self.valor_media<18:
                return f'Aluno {self.nome} em recuperação pois {self.valor_media}'
            else:
                return (f'Aluno {self.nome} aprovado pois {self.valor_media}')


aluno = Aluno('Marcos', [19.0, 19.0, 20.0])
print(aluno)