lista=[10, 30, 3, -5, 45, 2, 5, 25, 43, 62]
for e in lista:
    for f in range(1, 100):
        if e%f == 0:
            print(f'{f} é o multiplo de {e}')