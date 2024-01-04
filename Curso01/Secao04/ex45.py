"""
Faça um programa para converter uma letra maiuscula em letra minuscula. Use a tabela ASCII para resolver o problema
"""
e=False
while e != True:
    maiuscula=input("Digite uma letra maiuscula: ")
    print(f"valor de ASCII: {ord(maiuscula)}")
    minuscula=ord(maiuscula)+32
    print(f"Letra convertida: {chr(minuscula)}")