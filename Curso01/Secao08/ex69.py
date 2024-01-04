def fracao(numerador, denominador):
    lista=[]
    for a in range(1,min(numerador, denominador)):
        if numerador%a == 0 and denominador%a == 0:
            lista.append(a)
    divisor=max(lista)
    return (numerador/divisor)/(denominador/divisor)

fracao1=fracao(55, 20)
fracao2=fracao(80, 38)
print(fracao1+fracao2)
print(fracao1-fracao2)
print(fracao1*fracao2)
print(fracao1/fracao2)