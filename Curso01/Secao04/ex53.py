"""
Faça um programa para ler as dimensões de um terreno(comprimento c e largura l), 
bem como o preço do metro da tela p. imprima o custo para cercar este mesmo terreno com tela.
"""
comprimento=float(input("Insira o comprimento do terreno: "))
largura=float(input("Insira a largura do terreno: "))
preco_tela=float(input("Insira o preço da tela: "))

print(f"O terreno possuem {comprimento*largura}m² e custará para cercar R${((comprimento*largura)*2)*preco_tela}")