def consumo(distancia, litros):
    media= distancia/litros
    if media < 8:
        return "Veda o carro!"
    elif media >= 8 and media < 14:
        return "Econômico!"
    elif media > 14:
        return "Super econômico!"

print(consumo(380, 46))