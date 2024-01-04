import readchar

def getchar(n=500):
    lista=[]
    for _ in range(n):
        c = readchar.readchar()
        if c == '\r':
            break
        print(c)
        lista.append(c)
    return lista

print(getchar())