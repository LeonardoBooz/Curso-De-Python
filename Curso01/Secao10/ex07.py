lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pares = list(map(lambda x: x if x%2 == 0 else None, lista ))
pares = list(filter(lambda par: par != None, pares))
print(pares)