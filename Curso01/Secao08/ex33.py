from math import factorial
def soma_fatoracao(n):
    soma=0
    fatoracao=factorial(4)
    for a in str(fatoracao).split():
        soma+=int(a)
    return soma

print(soma_fatoracao(4))