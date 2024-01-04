def nota(n1, n2, n3 , letra='a'):
    if letra.lower() == 'a':
        return n1 + n2 + n3/3
    else:
        return (n1*5 + n2*3 + n3*2)/(10)
    
print(nota(10, 10, 10, 'p'))