"""
Faça um programa que leia o horário (hora, minuto e segundo) de inicio e a duração, em
segundos, de uma experiencia biologica. O programa deve resultar com o novo horario
(hora, minuto e segundo) do termino da mesma.
"""
from datetime import datetime


fim=False
def interromper():
    sair=str(input("Quando desejar finalizar a experiencia digite 'sair'"))
    if sair.lower()=="sair":
        return True
def calculo(hora_recebida):
    hora=int(str(hora_recebida[0:3]))
    minuto=int(str(hora_recebida[4:6]))
    segundo=int(str(hora_recebida[7:9]))
    hora_p_segundo=hora*3600
    minuto_p_segundo=minuto*60
    segundo+=hora_p_segundo+minuto_p_segundo
    return segundo
hora_inicial=str(datetime.now())[10:19]
print(hora_inicial)
while fim == False: 
    fim=interromper()
    hora_final=str(datetime.now())[10:19]
    print(hora_final)
    print(f"A duração da experiencia biológica foi de: {calculo(hora_final)-calculo(hora_inicial)}s")
