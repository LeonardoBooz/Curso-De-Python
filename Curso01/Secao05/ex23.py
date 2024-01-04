"""
Determine se um determinado ano ledo é bissexto. Sendo que um ano é bissexto se for
divisivel por 4000 ou ser for divisivel por 4 e não for divisivel por 100.
"""

ano=int(input("Digite qualquer ano para ver se é bissexto:"))

if ano%4 == 0 and ano%100 != 0:
    print(f"O ano de {ano} é bissexto!")
else:
    print(f"O ano de {ano} não é bissexto!")