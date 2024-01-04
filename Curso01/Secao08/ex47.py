def maiores_10(matriz):
    maiore=[]
    for a, b in enumerate(matriz):
        for c,d in enumerate(b):
            if d > 10:
                maiore.append(d)
    return len(maiore)

matriz=[[12,5,3,55], [25,20,1,5], [9,5,6,6], [2,4,24,89]]

print(maiores_10(matriz))