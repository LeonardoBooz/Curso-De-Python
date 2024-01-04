def fatorial_exponencial(num):
    fatorial1=0
    for a in range(num):
        fatorial1=(a-a)**a
    for b in range(num):
        fatorial=b**fatorial1
    return fatorial

print(fatorial_exponencial(5))