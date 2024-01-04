def soma_algarismos(num):
    soma=0
    if num < 0:
        return 'Número invalído.'
    for a in range(0, num+1):
        soma+=a
    return soma

print(soma_algarismos(3))