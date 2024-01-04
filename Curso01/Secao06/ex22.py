"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
uma sequencia arbitraria de notas(válidas no intervalo de 10 a 20) e que mostre na tela,
como resultado, a correspondente media aritmetica. O número de notas com que o aluno
pretenda efetuar o calculo não será fornecido ao programa, o qual terminará quando for
introduzido um valor que não seja válido como nota de aprovação
"""
con=True
e=0
total_notas=0
while con != False:
    nota=float(input("Digite sua nota de 10 á 20: "))
    if nota < 10 or nota > 20:
        print("Nota inválida")
    else:
        total_notas+=nota
        e+=1
    media=total_notas/e
    if media < 15:
        con=False