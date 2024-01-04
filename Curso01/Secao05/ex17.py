"""
Faça um programa que calcule e mostre a área de um trapézio.
"""

lista_nome_dados=['base maior', 'base menor', 'altura']
lista_de_dados=[]

for e in lista_nome_dados:
    dado=float(input(f"Digite a {e}: "))
    lista_de_dados.append(dado)
print(f"A área do trapézio é de, {((lista_de_dados[0]+lista_de_dados[1])*lista_de_dados[2])/2}")