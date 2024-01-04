"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá
ser informado o número de dados lidos e número de valores pares. O processo termina
quando for digitado o número 1000
"""


from random import randint 
h=True
j=0
e=0
parar=0
while parar != 1000:
    while h:
        g=randint(1,200)
        e+=1
        if g%2 == 0:
            j+=1
            print(f"{g} é par, total processado: {e} desses, {j} são pares")
        else:
            print(f"{g} não é par, total processado: {e} desses, {j} são pares")
        parar=int(input())