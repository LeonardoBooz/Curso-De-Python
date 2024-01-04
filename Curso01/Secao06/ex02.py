"""
Escreva um programa que escreva na tela de 1 até 100, de 1 em 1, 3 vezes. A primeira vez
deve usar a estrutura de repetição 'for', depois 'while' e depois 'do while' 
"""

for e in range(1,101):
    print(e)
f=0
while f != 100:
    f+=1
    print(f)
g=True
j=0
while g:
    j+=1
    print(j, end=", ")
    if j == 100:
        break