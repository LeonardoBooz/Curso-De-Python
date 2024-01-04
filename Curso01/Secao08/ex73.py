from random import randint, choice


def recebe_dados(n=1):
    l={
        'sexo': [], 
        'olhos': [],
        'cabelo':[],
        'idade': []
    }
    for a in range(n):
            l['sexo']+=[choice(['masculino', 'feminino'])]
            l['olhos']+=choice('AC'),
            l['cabelo']+=choice('LPC'),
            l['idade']+=[randint(1, 50)]
    return l["sexo"], l["olhos"], l["cabelo"], l["idade"]

def olhos_cabelos(olhos, cabelo, idade):
    soma=0
    for a, b  in zip(olhos, cabelo):
        if a == 'C' and b == 'P':
            for a in idade:
                soma+=a
    return soma/len(idade)

def anciao(*args):
    return max(args)

def idade_olhos_cabelos(sexo, olhos, cabelo, idade):
    soma=0
    for a, b, c, d in zip(sexo, olhos, cabelo, idade):
        if a == 'feminino' and d >= 18 and d<= 35 and b == 'A' and c == 'L':
             soma+=1
    return soma


sexo, olhos, cabelo, idade=recebe_dados(10)
lista=[]
print(olhos_cabelos(olhos, cabelo, idade))
print(anciao(*idade))
print(idade_olhos_cabelos(sexo, olhos, cabelo, idade))