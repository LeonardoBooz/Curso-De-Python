media=[]
nota_final=[]
turma=[[10, 7, 8],[11, 8, 5],[12, 10, 9]]
for a, b in enumerate(turma):
    nota_final+=[b[1]+b[2]]
    media+=[f'Matricula: {b[0]} nota final: {b[1]+b[2]}']
print(max(media))
print(f'A media aritmética é: {sum(nota_final)/3:.2f}')