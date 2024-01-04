from pdferli import get_pdfdf
from PrettyColorPrinter import add_printer
import pandas as pd
import numpy as np
add_printer(1)
path = r'C:\Curso\pdf_com_python\modelo_de_nota_de_envio_de_amostra.pdf'
df = get_pdfdf(path, normalize_content = False)
df = np.split(df, df.loc[df.aa_element_type == 'LTAnno'].index)
togi = []
for r in df:
    df2 = r.dropna(subset='aa_size')
    if not df2.empty:
        df3 = df2.sort_values(by = 'aa_x0')
        togi.append(df3.iloc[:1])
group6 = []
togi = pd.concat(togi)
togi.loc[:, 'x0round'] = togi.aa_x0.round(2)
for name, group in togi.groupby('x0round'): 
    if len(group) > 1:
        group2 = group.reset_index(drop=True)
        group3 = np.split(group2, group2.loc[group2.aa_element_type == 'Helvetica-Bold'].index)
        for group4 in group3:
            if len(group4) >1:
                group5 = (group4.sort_values(by='bb_hierachy_page'))
                group6.append(group5['aa_text_element'])
dados = pd.concat(group6, axis= 0).drop_duplicates()
dados = dados.reset_index(drop=True)

print(dados)