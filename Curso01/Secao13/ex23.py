lista=[['Mecânico', '5 anos'], ['Almoxarife', '10 anos'], ['Controle de Qualidade', '25 anos'],
    ['Programador CNC', '6 anos'], ['Tecnico de Segurança', '8 anos']
    ]
with open(r'C:\Curso\Curso01\Secao13\emp.txt', 'w') as arq:
    for a in lista:
        a = ', '.join(a)
        arq.write(f'{a}\n')