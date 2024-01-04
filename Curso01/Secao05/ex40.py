preco=float(input("Digite o preço do carro: "))
if preco <= 12_000:
    print(f"O veículo custara: {preco*0.05+preco}")
elif preco > 12_000 and preco <= 25_000:
    print(f"O veículo custara: {(preco*0.10+preco)+(preco*0.15)}")
elif preco > 25_000:
        print(f"O veículo custara: {(preco*0.15+preco)+(preco*0.20)}")