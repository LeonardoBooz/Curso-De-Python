def hiper_fatorial(n):
    hf=1
    for a in range(1, n+1):
        hf *= ((a)**a)*(a**a)
    return hf

print(hiper_fatorial(5))