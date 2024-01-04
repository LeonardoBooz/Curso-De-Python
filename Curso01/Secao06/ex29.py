import math 

num=int(input("Digite um número: "))
total=0
for e in range(2, num +2):
    for f in range(1, num):
        total+=f/math.factorial(e)
print(f"O valor de E é: {total}")