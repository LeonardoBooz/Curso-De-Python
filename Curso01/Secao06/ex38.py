"""
Faça um programa que calcule o terno pitagórico a ,b, c para qual a+b+c=1000. Um terno
pitagórico é um conjunto de três números naturais, a, b, c, para qual a²+b²=c²
"""
import math

num1=int(input("Digite o valor de 'a²': "))
num2=int(input("Digite o valor de 'b²': "))
total=math.sqrt((num1**2)+(num2**2))
if total-int(total)!=0:
    print(f"{num1} e {num2}, não formam um terno pitagórico")
else:
    print(f"O valor de 'c' é {total}²")