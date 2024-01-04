#Leia um número de 4 digitos (de 1000 a 9999) e imprima um digito por linha

num=int(input("Digite um número de 1000 á 9999"))
n=1
j=2
for e in range(len(str(num))):

    if e == 0:
        numero=int(str(num)[0:1])
    else:
        numero=int(str(num)[n:j])
        n+=1
        j+=1
    print(numero)