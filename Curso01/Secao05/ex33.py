
def avaliador(preco):
    if preco <= 80:
        return "barato"
    elif preco > 80 and preco <=120:
        return 'normal'
    elif preco > 120 and preco <= 200:
        return 'caro'
    else:
        return 'muito caro'

preco=float(input("Digite o preço atual do produto: "))

if preco <= 50:
    preco_novo=(preco*0.05)+preco
    saida=(f"O preço de {preco_novo} esta {avaliador(preco_novo)}")
elif preco > 50 and preco <= 100:
    preco_novo=(preco*0.10)+preco
    saida=(f"O preço de {preco_novo} esta {avaliador(preco_novo)}")
elif preco > 100:
    preco_novo=(preco*0.15)+preco
    saida=(f"O preço de {preco_novo} esta {avaliador(preco_novo)}")
print(saida)