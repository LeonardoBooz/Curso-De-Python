"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus
Celsius. A formula de conversão é: C=5*(F-32)/9, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit
"""

num=float(input("Digite a temperatura em Fahrenheit: "))
print(f'Graus Celsius: {(5*(num-32)/9)}')