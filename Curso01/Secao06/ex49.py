

salario_Carlos=float(input("Insira o salário de Carlos"))
salario_Joao=salario_Carlos/3
salario_per_ca=0
salario_per_jo=0
meses=0
for e in range(1,300):
    salario_per_ca+=salario_Carlos
    salario_per_jo+=salario_Joao
    poup_liq_jo=(salario_per_jo*3)+salario_per_jo
    poup_liq_ca=(salario_per_ca*0.02)+salario_per_ca
    meses+=1
    if poup_liq_ca < poup_liq_jo:
        break
print(f"A uma taxa de 300%, João ultrapassa Carlos em {meses} meses")