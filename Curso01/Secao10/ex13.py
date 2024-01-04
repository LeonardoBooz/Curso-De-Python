from random import choice, randint, seed
from collections import Counter
#seed(2)


def verifica_faixa_etaria(chave1, chave2, param1, param2, lista_a_ser_filtrada):
    filtrado = list(map(lambda element: element[chave1] if element[chave2] >= param1 and element[chave2] <= param2 else None, lista_a_ser_filtrada))
    filtrado = list(filter(lambda element: element != None, filtrado))
    if bool(filtrado) == False:
        return 'Não encontrado'
    return Counter(filtrado)


lista_a_ser_filtrada=[]
for _ in range(1000):
    lista_a_ser_filtrada.append({
                        'pessoa': choice(['Francisco', 'Miguel', 'Manuel', 'António', 'José', 'João', 'Tomás', 'Pedro', 'Luís', 'Carlos', 'Augusto', 'Alfredo', 'André', 'Bento', 'Diogo', 'Fernando', 'Martim', 'Isabel', 'Catarina', 'Rita']),
                        'cor_pele' : choice(['branco', 'preto', 'pardo']),
                        'cor_olhos' : choice(['castanho', 'marrom', 'verde', 'azul']),
                        'cor_cabelos' : choice(['loiro', 'moreno', 'ruivo', 'preto']),
                        'idade' : randint(1, 66),
                        'celular' : choice(['Apple', 'Samsung', 'LG', 'Motorola', 'Xiomi'])
                    })

# print(lista_a_ser_filtrada)

#Filtrar o nome das pessoas que tem olhos azuis
filtro_cor_olhos = list(map(lambda pessoas: pessoas['pessoa'] if pessoas['cor_olhos'] == 'azul' else None, lista_a_ser_filtrada))
filtro_cor_olhos = list(filter(lambda cor: cor != None, filtro_cor_olhos))
if bool(filtro_cor_olhos) == False:
    filtro_cor_olhos = 'Não encontrado'
print(filtro_cor_olhos)
#Filtrar quem tem entre 18 e 25 e retornar qual é o cabelo mais comum
print(min(verifica_faixa_etaria('cor_cabelos', 'idade',18,25, lista_a_ser_filtrada)))
# Identificar qual é a marca de celular mais utilizada 
celulares = list(map(lambda pessoa: pessoa['celular'], lista_a_ser_filtrada))
print(max(Counter(celulares)))
#Descobrir qual é o celular preferido das faixas etarias entre 18 e 25, 30 e 40, e, 50 e 60.
print(max(verifica_faixa_etaria('celular', 'idade', 18, 25, lista_a_ser_filtrada)))
print(max(verifica_faixa_etaria('celular', 'idade', 30, 40, lista_a_ser_filtrada)))
print(max(verifica_faixa_etaria('celular', 'idade', 50, 60, lista_a_ser_filtrada)))
#Dar a porcentagem de brancos, pretos e pardos
filtrar_cor_pele = list(map(lambda pessoa: pessoa['cor_pele'], lista_a_ser_filtrada))
cor_pele = Counter(filtrar_cor_pele)
percent= list(map(lambda f: f'{cor_pele[f]/len(filtrar_cor_pele)*100:.2f}% {f}', cor_pele))
print(percent)

