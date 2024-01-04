with open(r'C:\Curso\Curso01\Secao13\carrinho_compras.txt') as compras:
    lista_preco = []
    for a in compras:
        item, preco = a.split(', ')
        lista_preco.append(float(preco))
    print(compras.read())
print(f'Total a apagar: {sum(lista_preco):.2f}')