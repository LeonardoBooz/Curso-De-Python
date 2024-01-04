"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de laboratório:
2; Avaliação semestral: 3; Exame final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado
(média entre 0 e 2.9), de recuperação (entre 3 e 4.9) ou se foi aprovado. 
 """


def calculadore_media():
    lista_nota=[]
    avaliacoes=['Trabalho de laboratório', 'Avaliação semestral', 'Exame final']

    for e in avaliacoes:
        nota=float(input(f"insira a nota de {e}: "))
        if e == 'Trabalho de laboratório':
            if nota >= 0 and nota <=2:
                lista_nota.append(nota)
            else:
                print("Nota invalida")
                calculadore_media()
        if e == 'Avaliação semestral':
            if nota >= 0 and nota <=3:
                lista_nota.append(nota)
            else:
                print("Nota invalida")
                calculadore_media()
        if e == 'Exame final':
            if nota >= 0 and nota <=5:
                lista_nota.append(nota)
            else:
                print("Nota invalida")
                calculadore_media()
    media=sum(lista_nota)
    if media == 0 and media >= 2.9:
        print(f"O aluno esta reprovado, média: {media}")
        exit()
    elif media == 3 and media >= 4.9:
        print(f"O aluno em recuperação, média: {media}")
        exit()
    else:
        print(f"O aluno esta aprovado, média: {media}")
        exit()


calculadore_media()