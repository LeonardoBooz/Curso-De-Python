def funcoes(vetor,opc=1):
    if opc == 1:
        return vetor
    elif opc == 2:
        return vetor[::-1]
    elif opc == 3:
        return sum(vetor)/len(vetor)
    
print(funcoes([2,5,8,6,4,2,4,5], 1))