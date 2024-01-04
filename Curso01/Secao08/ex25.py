def funcao(n):
    soma=0
    for a in range(0, n+1):
        soma+=((a**2)+1)/(n+3)
    return soma

print(funcao(25))