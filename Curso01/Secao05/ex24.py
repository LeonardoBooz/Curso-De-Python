"""
Uma empresa vende o mesmo produto para quatro diferente estados. Cada estado
possui um ataxa diferente de imposto sobre o produto. Faça um programa em que 
o usuário entre com o valor e o estado destino do produto e o programa retorne o
preço que ele será vendido. Se o estado digitado não dor válido, mostrar uma menssagem
de erro
"""

lista_nome_dados=['preço do produto', 'estado destino']
lista_dados=[]
for e in lista_nome_dados:
    dado=input(f"Digite o {e}")
    lista_dados.append(dado)
preco_produto=int(lista_dados[0])
if lista_dados[1] == 'mg' or 'minas gerais':
    print(f"O preço do produto com o imposto de MG é: R${(preco_produto*0.7)+preco_produto}")
elif lista_dados[1] == 'sp' or 'sao paulo' or 'são paulo':
    print(f"O preço do produto com o imposto de SP é: R${(preco_produto*0.12)+preco_produto}")
elif lista_dados[1] == 'rj' or 'rio de janeiro':
    print(f"O preço do produto com o imposto de RJ é: R${(preco_produto*0.15)+preco_produto}")
elif lista_dados[1] == 'ms' or 'mato grosso do sul':
    print(f"O preço do produto com o imposto de MS é: R${(preco_produto*0.8)+preco_produto}")
else:
    print("UF não disponivel!")