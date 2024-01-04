def retorna_string(a):
    try:
        return a[0]
    except IndexError:
        return -1
    
print(retorna_string(''))