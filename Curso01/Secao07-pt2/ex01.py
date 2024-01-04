a = [[12,3,4,43],[2,3,4,5],[15,16,21,2],[12,7,6,10]]
cont=0
for e in a:
    for f in e:
        print(f)
        if f > 10:
            cont+=1
print(f'São maior que 10, {cont} números')
