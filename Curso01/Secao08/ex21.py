def verifica_primo(num):
    for a in range(2, num):
        if num != a and num%a == 0:
            print('Não é primo')
            return False
    return True

lista=[]
for a in range(2,100):
    if verifica_primo(a):
        lista.append(a)
print(lista)