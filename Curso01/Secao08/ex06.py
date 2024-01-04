def converte_em_segundos(hora,minuto,segundo):
    segundo+= (hora*3600)+(minuto*60)
    return f'total de segundos, {segundo}'
    
print(converte_em_segundos(5,60,35))