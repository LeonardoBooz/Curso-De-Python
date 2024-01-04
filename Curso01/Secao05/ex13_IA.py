"""
Faça um algoritomo que calcule a média ponderada das notas de 3 provas. A primeira e
a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual 
ou superior a 60 pontos
"""

def calcular_media_ponderada(nota1, nota2, nota3):
    peso1, peso2, peso3 = 1, 1, 2
    media_ponderada = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)
    return media_ponderada

def verificar_aprovacao(media):
    if media >= 60:
        return "Aprovado"
    else:
        return "Reprovado"

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = calcular_media_ponderada(nota1, nota2, nota3)
resultado = verificar_aprovacao(media)

print(f"A média do aluno é {media:.2f}")
print(f"O aluno foi {resultado}")
