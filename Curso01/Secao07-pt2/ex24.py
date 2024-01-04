maior=0
matriz=[
    [55,79,14,29,93,71,40,67,53,88,30,3],
    [4,60,11,42,69,24,68,56,1,32,56,71],
    [51,79,63,89,41,92,36,54,22,40,40,28],
    [99,3,45,2,44,75,33,53,78,36,84,20],
    [64,23,67,10,26,38,40,67,59,54,70,66],
    [2,62,12,20,95,63,94,39,63,8,40,91],
    [66,73,99,26,97,17,78,78,96,83,14,88],
    [75,0,76,44,20,45,35,14,0,61,33,97],
    [22,75,31,67,15,94,3,80,4,62,16,14],
    [96,35,31,47,55,58,24,0,17,54,24,15],
    [35,71,89,7,5,44,44,37,44,60,21,58],
    [5,94,47,69,28,73,92,13,86,52,17,77]
]
for a in range(9):
    for b in range(9):
        produto=matriz[a][b]*matriz[a+1][b+1]*matriz[a+2][b+2]*matriz[a+3][b+3]
        maior=(max(produto, maior))
    for c in range(9):
        produto=matriz[a][-c-1]*matriz[a+1][-c-2]*matriz[a+2][-c-3]*matriz[a+3][-c-4]
        maior=(max(produto, maior))
    for d in range(9):
        produto=matriz[a][d]*matriz[a][d+1]*matriz[a][d+2]*matriz[a][d+3]
        maior=(max(produto, maior))
    for e in range(9):
        produto=matriz[e][a]*matriz[e+1][a]*matriz[e+2][a]*matriz[e+3][a]
        maior=(max(produto, maior))
print(maior)