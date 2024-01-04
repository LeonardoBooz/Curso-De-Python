def verifica_anagrama(a, b):
    to_String=f'{a} não é um anagrama de {b}'
    if len(a) == len(b):
        for c in a:
            if c not in b:
                return to_String
    else:
        return to_String
    return f'{a} é um anagrama de {b}'

print(verifica_anagrama('armo', 'roma'))