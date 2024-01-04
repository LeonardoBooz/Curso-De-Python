def dois_numeros():
    lista_ord=['primero', 'segundo']
    lista_num=[]
    for e in lista_ord:
        num=int(input("digite um  número: "))
        lista_num.append(num)
    return lista_num


opc=int(input("Escolha a opção: \n"+
        "1-Soma de 2 números\n"+
        "2-Diferença entre 2 números\n"+
        "3-Produto entre 2 números\n"+
        "4-Divião entre 2 números\n"))
lista_num=dois_numeros()
if opc == 1:
    print(f"A soma dos  dois números: {lista_num[0]+lista_num[1]}")
elif opc == 2:
    
    if lista_num[0] < lista_num[1]:
        print(f"A diferença dos  dois números: {(lista_num[0]-lista_num[1])*-1}")
    else:
        print(f"A diferença dos  dois números: {lista_num[0]-lista_num[1]}")

elif opc == 3:
    print(f"O produto dos  dois números: {lista_num[0]*lista_num[1]}")
elif opc == 4:
    try:
        print(f"A divisão dos dois números: {lista_num[0]/lista_num[1]}")
    except ZeroDivisionError:
        print("Não é possível fazer divisão por zero!")
else:
    print("opção invalida")