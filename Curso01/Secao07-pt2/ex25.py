from random import randint


def print_tabuleiro():
    for a in tabuleiro:
        print(a)

def verifica_vitoria():
    soma_zero=0
    fim=False
    for b in range(0,3):
        if -1 == tabuleiro[b][0] and -1 == tabuleiro[b][1] and -1 == tabuleiro[b][2]:
            print("Parabéns, você venceu!")
            fim=True
        elif 1 == tabuleiro[b][0] and 1 == tabuleiro[b][1] and 1 == tabuleiro[b][2]:
            print('Você é a prova de que os robôs vão substituir as pessoas!!!')
            fim=True
        elif -1 == tabuleiro[0][b] and -1 == tabuleiro[1][b] and -1 == tabuleiro[2][b]:
            print("Parabéns, você venceu!")
            fim=True
        elif 1 == tabuleiro[0][b] and 1 == tabuleiro[1][b] and 1 == tabuleiro[2][b]:
            print('Você é a prova de que os robôs vão substituir as pessoas!!!')
            fim=True
    if -1 == tabuleiro[0][0] and -1 == tabuleiro[1][1] and -1 == tabuleiro[2][2]:
        print("Parabéns, você venceu!")
        fim=True
    elif 1 == tabuleiro[0][0] and 1 == tabuleiro[1][1] and 1 == tabuleiro[2][2]:
        print('Você é a prova de que os robôs vão substituir as pessoas!!!')
        fim=True
    elif -1 == tabuleiro[0][2] and -1 == tabuleiro[1][1] and -1 == tabuleiro[2][0]:
        print("Parabéns, você venceu!")
        fim=True
    elif 1 == tabuleiro[0][2] and 1 == tabuleiro[1][1] and 1 == tabuleiro[2][0]:
        print('Você é a prova de que os robôs vão substituir as pessoas!!!')
        fim=True
        
    for c in range(0,3):
        soma_zero+=tabuleiro[c].count(0)
    if soma_zero == 1:
        print('Você consegui empatar com uma inteligencia tão burra como essa?')
        fim=True
    return fim

jogadas=[]
tabuleiro=[[0, 0, 0],[0, 0, 0],[0, 0, 0]]
hum_jogou=False
print('\t#Bem vindo ao jogo da velha# \nSe você digitar uma posição ja escolhida perdera sua vez'+
      '\nDigite neste formato, 1,2 para escolher qual posição marcar..')
print()
qnt_turnos=0
while True:
    qnt_turnos+=1
    if qnt_turnos == 1:
        jogador_comeca=randint(0,1)
        print_tabuleiro()
        if jogador_comeca == 0:
            jogada=input("De a sua primeira jogada: ")
            hum_jogou=True
        else:
            print("O robô começa...")
            jogada=f'{randint(0,2)},{randint(0,2)}'
    else:
        if hum_jogou == True:
            print("Vez do robô ...")
            jogada=f'{randint(0,2)},{randint(0,2)}'
            hum_jogou=False
        else:
            jogada=input('É sua vez...')
            hum_jogou=True
    if jogada in jogadas:
        print('Posição invalida!!!')
    else:
        posi=jogada.split(',')
        jogadas.append(jogada)
        if hum_jogou == True:
            print('jogada humano',end=' ')
            tabuleiro[int(posi[0])][int(posi[1])]=-1
        else:
            print('jogada robo', end=' ')
            tabuleiro[int(posi[0])][int(posi[1])]=1
        print(jogada)
        print_tabuleiro()
        print()
    if verifica_vitoria() == True:
         print("Fim de Jogo!")
         exit()