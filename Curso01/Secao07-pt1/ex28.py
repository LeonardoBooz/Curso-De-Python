vetor=1, 3 , 4 ,56 ,21 ,4 ,5 ,543 ,4 ,54
vetor1=[]
vetor2=[]
for e in vetor:
    if e%2 == 0:
        vetor1.append(e)
    else:
        vetor2.append(e)
print(vetor1)
print(vetor2)