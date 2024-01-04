"""
Faça um prova de matemática para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre
na tela a pergunta: 'Qual é a soma de a+b, onde a e b são os números aleatórios.'
Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e
 as respostas corretas, além de quantas vezez o aluno acertou
"""


from random import randint

lista_de_resultados=[]
acertos=0

for e in range(5):
    a=randint(1,100)
    b=randint(1,100)
    total=a+b
    resposta=int(input(f'=========Pergunta nº{e+1}===========\n'+
        f"          Quanto é {a}+{b}?\n"))
    if total == resposta:
        lista_de_resultados.append(f'Você acertou a nº{e+1}! Sua resposta, {resposta}, resultado {total}\n')
        acertos+=1
    else:
        lista_de_resultados.append(f'Você errou a nº{e+1}! Sua resposta, {resposta}, resultado {total}\n')
for e in lista_de_resultados:
    print(e)
print(f'Acertou, {acertos}/5')