def media(*args):
    return f'R${float(sum(args)/len(args)):.2f}'

print(media(*[23,445,4,57,65,434,4]))

