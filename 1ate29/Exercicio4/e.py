def decorador(func, *args, **kwargs):
    def media():
        medias = func()
        i = 0
        for media in medias:
            if (media >= 9.5):
                i += 1
        print("numero de alunos com media > 9.5",i)

    return media

@decorador
def pedeNota():
    medias=[]
    for i in range (3):
        print("Aluno",i+1)
        notas = 0
        for c in range (4):
            notas = notas + float(input(str(c+1) + "Nota:"))
        notas = notas / 4
        medias.append(notas)
    return medias

pedeNota()