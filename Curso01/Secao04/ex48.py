#Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

segundos=0
minutos=0
horas=0
con=False

segundos=int(input("Digite os segundos para conversão: "))
while con == False:
    if segundos > 59:
        minutos +=1
        segundos-=60
    elif minutos > 59:
        horas +=1
        minutos-=60
    else:
        con=True
print("=================================\n"+
    "        Relóginho 2000\n"+
    "___________\n"
    f"|{horas}h:{minutos}m:{segundos}s|")