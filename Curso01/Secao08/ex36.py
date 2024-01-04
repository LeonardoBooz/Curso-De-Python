from math import factorial
def super_fatorial(n):
    produto=1
    for a in range(1, n+1):
        produto=produto*factorial(a)
    return produto

print(super_fatorial(4))