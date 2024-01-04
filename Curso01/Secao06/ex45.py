"""
Faça um algoritimo que converta uma velocidade expressa em km/h para m/s e vice versa. Você deve
criar um menu com as duas opções de conversão e com uma opção para finalizar o programa. O usuário
poderá dazer quantas conversões desejar, sendo que o programa só será finalizado quando a opção de 
finalizar for escolhida.
"""

cont=False
while cont == False:
    opc=int(input('Escolha entre as opções abaixo: \n'+
                  '(1)-Km/h\n'+
                  '(2)-m/s\n'+
                  '(3)-Finalizar'))
    if opc < 1 or opc > 3:
        print("Opção invalida!")
        breakpoint
    elif opc == 1:
        velocidade=float(input('Digite o valor de Km/h: '))
        print(f'convertido para m/s: {velocidade/3.6}')
    elif opc == 2:
        velocidade=float(input('Digite o valor de m/s: '))
        print(f'convertido para Km/h: {velocidade*3.6}')
    elif opc == 3:
        cont=True
