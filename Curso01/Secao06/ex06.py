num=[]
for e in range(1,11):
    num.append(int(input(f"Digite um número {e}/10: ")))
print(f'Total={sum(num)} e media={sum(num)/10}')