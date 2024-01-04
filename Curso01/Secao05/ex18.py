"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações 
matematicas(as básicas, por exemplo). O usuário escolhe uma das opções e 
seu programa então pede dois valores númericos e realiza a operação, mostrando
o resultado saindo.
"""
    

def calculadora(ope):
    if ope == '+' or ope == '-' or ope == '*' or ope == '/':
        pass
    else:
        print("Operador invalido")
        exit()
    lista_de_numeros=[]
    lista_ord=['primeiro', 'segundo']
    for i in lista_ord:
        num=float(input(f"Digite o {i} número: "))
        lista_de_numeros.append(num)
    num1=lista_de_numeros[0]
    num2=lista_de_numeros[1]
    if ope == '+':
        total=num1+num2
    elif ope == '-':
        total=num1-num2
    elif ope == '*':
        total=num1*num2
    else:
        total=num1/num2
    return f"O resultado é: {total}"

ope=input("            Calculadora 5000\n"+
      "escolha entre as opções abaixo:\n"+
      "Adição, digite '+'\n"+
      "Subtração, digite '-'\n"+
      "Multiplicação, digite '*'\n"+
      "Divisão, digite '/'\n"+
      "===============================\n"
    )
print(calculadora(ope))