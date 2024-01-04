def divide_pares_impares(*vetor):
    a=[] 
    b=[]
    for c in vetor:
        if c%2==0:
            a.append(c)
        else:
            b.append(c)
    return a, b

print(divide_pares_impares(*[50, 50, 656, 2, 65, 650, 65, 656, 565, 5, 6055, 45, 6256, 506, 532, 320, 32, 502, 15, 102, 12, 12, 15, 0, 52, 12, 151, 21, 52, 42,2]))