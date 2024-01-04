def fator_primo(num):
    maior=[]
    for a in range(2, num+1):
        fracao=num/a
        if fracao == int(fracao):
            fracao=int(fracao)
            if verifica_primo(fracao):
                maior.append(fracao)
    return max(maior)

def verifica_primo(maior):
    for a in range(2, maior):
        if maior != a and maior%a == 0:
            print('Não é primo')
            return False
    return True

print(fator_primo(70))
