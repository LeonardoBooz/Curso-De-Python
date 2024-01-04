lista=[1,2,12,5,54,545,45,4,8,651,5,145,454,54,54,]
pares = list(map(lambda x: True if x%2 == 0 else False, lista))
print(pares)