def intercador(str1, str2):
    e=0
    nova_str=''
    tamanho1=len(str1)
    tamanho2=len(str2)
    diferença=tamanho1-tamanho2
    if tamanho1 != tamanho2:
        e_menor=True
        if max(tamanho1, tamanho2) == tamanho1:
            maior=str1
            menor=str2
        else:
            maior=str2
            menor=str1
    else:
        e_menor=False
        menor=str1
        maior=str2
    for a,b in zip(menor, maior):
        if e == 0:
            nova_str+=a
            e=1
        elif e==1:
            nova_str+=b
            e=0
    if e_menor:
        nova_str+=maior[diferença:]
    return nova_str

print(intercador('ana', 'banana'))