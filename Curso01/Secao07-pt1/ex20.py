lista1=[]
num=''
for e in range(50):
    if len(num) < 8:
        num+=str(e)
    else:
        lista1.append(int(num))
        num=''
print(lista1)