from random import choice
# a=dict(one=1, two=2, three=3)
# b={'one':[1,2,3], 'two':2, 'three':3}
# c=dict(zip(['one', 'two', 'three'],[1 ,2 ,3]))
# print(b['one'])
# print(list(b))
# loiro=2
# moreno=3
# ruivo=8
# d={'cabelo':[loiro, moreno, ruivo],
#    'sexo':{'feminino':5, 'masculino':8},
#    'olho':[{'verde':5,'azul':4,'marrom':4}],
#    'idade':[18, 22, 36, 5, 2, 50, 8, 7, 12, 20, 60, 28, 40]}
# print(a['olho'][0]['verde'])
# print(a['sexo']['masculino'])
# print(max(a['idade']))
lista_de_pessoas=[]
pessoa='jose'
cabelo='Preto'
sexo='Masculino'
olho='Marrom'
idade=45
e={pessoa:{
    'cabelo' : cabelo,
    'sexo' : sexo,
    'olho' : olho,
    'idade' : idade
    }
}
# print(e)
pessoa='Angela'
cabelo='loira'
sexo='Feminino'
olho='Marrom'
idade='21'
f={pessoa:{
    'cabelo' : cabelo,
    'sexo' : sexo,
    'olho' : olho,
    'idade' : idade
    }
}
# print(f)
pessoa='Marcia'
cabelo='Preto'
sexo='Feminino'
olho='verde'
idade='30'
g={pessoa:{
    'cabelo' : cabelo,
    'sexo' : sexo,
    'olho' : olho,
    'idade' : idade
    }
}
lista_de_pessoas.append(f)
lista_de_pessoas.append(e)
lista_de_pessoas.append(g)

# print(lista_de_pessoas)
idade=0
mais_velho=0
cor_do_cabelo={}
for a in lista_de_pessoas:
    print(a)
    for b in a:
        if int(a[b]['idade']) > mais_velho:
            mais_velho=int(a[b]['idade'])
        try:
            cor_do_cabelo[a[b]['cabelo']]+=[b]
        except KeyError:
            cor_do_cabelo[a[b]['cabelo']]=[b]
print(cor_do_cabelo)
print(choice(['cleiton', 'leo', 'vitor']))