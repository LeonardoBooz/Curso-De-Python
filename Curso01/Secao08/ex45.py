import math
def desvio_padrao(vetor):
    variacao=[]
    media=sum(vetor)/len(vetor)
    for a in vetor:
        variacao.append((media-a)**2)
    return math.sqrt(sum(variacao)/len(vetor))

print(desvio_padrao([2,3,4,3,65,3,54,5,3,4,5,6,7,3,354,5,5]))