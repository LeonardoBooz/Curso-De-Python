"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Jm/l e escreva uma mensagem de acordo com a tabela...
"""

lista_nome_dados=['Km percorridos', 'litros consumidos']
lista_dados=[]

for e in lista_nome_dados:
    num=float(input(f'Digite quantos {e}: '))
    lista_dados.append(num)

consumo=lista_dados[0]/lista_dados[1]

if consumo < 8:
    print("vende essa bagaça!")
elif consumo >= 8 and consumo <= 14:
    print("Econômico")
else:
    print("Super Econômico")