"""
Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 
100 números naturais e o quadrado da soma.
"""

soma=0
for e in range(1,100):
    soma+=e**2
print(f"A diferença é de {(soma**2)-soma}")