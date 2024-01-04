"""
Escreva um programa que receba como entrada o valor do saque realizado pelo
cliente de um banco e retorne quantas notas de cada valor serão nescessarias
para atender ao saque com a menor quantidade possivel de notas.
"""
qnt_100=0
qnt_50=0
qnt_20=0
qnt_10=0
qnt_5=0
qnt_2=0
qnt_1=0

valor=float(input("Digite o valor que deseja: "))
while valor != 0:
    if valor >= 100:
        valor-=100
        qnt_100+=1
    elif valor >= 50:
        qnt_50+=1
        valor-=50
    elif valor >= 20:
        qnt_20+=1
        valor-=20
    elif valor >= 10:
        qnt_10+=1
        valor-=10
    elif valor >= 5:
        qnt_5+=1
        valor-=5
    elif valor >= 2:
        qnt_2+=1
        valor-=2
    elif valor >= 1:
        qnt_1+=1
        valor-=1


print(f"Precisa de {qnt_100}un. notas de R$100\n"+ 
      f"Precisa de {qnt_50}un. notas de R$50\n"+
      f"Precisa de {qnt_20}un. notas de R$20\n"+
      f"Precisa de {qnt_10}un. notas de R$10\n"+
      f"Precisa de {qnt_5}un. notas de R$5\n"+
      f"Precisa de {qnt_2}un. notas de R$2\n"+
      f"Precisa de {qnt_1}un. notas de R$1")
