def calculadora(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '/':
        return n1 / n2
    elif op == '*':
        return n1 * n2
    
print(calculadora(5, 5, '-'))