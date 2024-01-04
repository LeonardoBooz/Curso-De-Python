"""
Leia um temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C=K-273,15, sendo C a temperatura em Celsius e K em Kelvin
"""

num=float(input('Digite a temperatura em Kelvin: '))
print(f"Graus Celsius: {num-273.15}")