def simplifica(numerador, denominador):
    menor=0
    n=min(numerador, denominador)
    for a in range(n-1, 2, -1):
        fracao=n/a
        if fracao == int(fracao):
            menor=min(n, fracao)
    denominador=menor
    numerador=menor
    return numerador, denominador

print(simplifica(36, 60))