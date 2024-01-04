import math 

num=int(input("Digite um número: "))
total=0
for e in range(1, num +1):
    total+=e/math.factorial(e)
print(f"O valor de E é: {total}")

