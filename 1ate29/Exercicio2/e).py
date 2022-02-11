def nota():

    while True:
        try:
            nota1 = float(input("introduza  a nota do aluno:"))
            nota2 = float(input("introduza  a nota do aluno:"))
            media = (nota1 + nota2) / 2
            print(media)

            if media >= 9.5 and media < 19:
                print('Aprovado')
            elif media > 19:
                print('Aprovado com destinção')

            elif media < 9.5:
                print('Reprovado')

            else:
                print('Opção inválida')

        except ValueError as err:
            print("opção inválida", err)



nota()

