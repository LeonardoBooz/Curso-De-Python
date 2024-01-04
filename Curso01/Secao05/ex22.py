"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode
ou não se aposentar.
"""


lista_nome_dados=['qual a sua idade?', 'quanto tempo de serviço?']
lista_dados=[]

for e in lista_nome_dados:
    num=(int(input(f"Digite {e}")))
    lista_dados.append(num)

if lista_dados[0] >= 65:
    print("Pode se aposentar companheiro pela idade!")
elif lista_dados[1] >= 30:
    print("Ja trabalhou bastante, pode se aposentar por tempo de contribuição!")
elif lista_dados[0] >= 60 and lista_dados[1] >=25:
    print("Quase que não deu pra tu! Pode ser aposentar")
else:
    print("Não vai dá coléga, volta a trabalhar!")