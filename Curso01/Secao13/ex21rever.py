with open('Alunos_binarios.bin', 'wb') as arq:
    lista_alunos ='Ana, 10.0 Joao, 8.0 Mateus, 9.0'
    arq.write(lista_alunos.encode())
with open('Alunos_binarios.bin', 'rb') as arq:
    alunos = list(map(lambda x: x.decode(), arq.readlines()))
for a in alunos:
    a[-2]


#     if maior < int(nota):
#         maior = int(nota)
#         lista_maiores.append(a)
# print(lista_maiores[-1])