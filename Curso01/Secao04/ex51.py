"""
Escreva um programa que leia as coordenadas x e y de pontos no r² e calcule sua 
distancia de origem(0,0)
"""
import math

x=float(input("Digite a coordenada x: "))
y=float(input("Digite a coordenada y: "))
print(f"A distancia de origem é {math.sqrt((x**2)+(y**2))}")
