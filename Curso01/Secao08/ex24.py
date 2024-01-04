def blaze(n1):
    n2 = (n1 * 2)
    for i in range(0, n1):                
        for _ in range(0, n2):
                print(end=' ')
        n2 -= 1
        for _ in range(0, i + 1):
            print('*', end=' ')
        print()
blaze(6)