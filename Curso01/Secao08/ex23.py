def faz_piramede(num):
    for b in range(0, num):
        c='*'*b
        print(c)
    for b in range(num, 0, -1):
        c='*'*b
        print(c)

num=int(input('Digite um número: '))
faz_piramede(num)