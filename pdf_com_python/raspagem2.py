from pdferli import get_pdfdf
from PrettyColorPrinter import add_printer
import pandas as pd
import numpy as np

add_printer(1)

path = r'C:\Curso\pdf_com_python\Sem título 1.pdf'

df = get_pdfdf(path)
df = np.split(df, df.loc[df.aa_element_type == 'LTAnno'].index)
df = pd.concat(df)
df = df.sort_values('aa_x0')
df = df.reset_index(drop=True)
df = df['aa_text_element'].drop_duplicates()
print(df)

def getNome(df: pd.DataFrame):
    return str(df.to_numpy()[2][11:])

def getInicioVigencia(df: pd.DataFrame):
    return str(df.to_numpy()[11])

def getFinalVigencia(df: pd.DataFrame):
    return str(df.to_numpy()[12])

def getPremioTotal(df: pd.DataFrame):
    return str(df.to_numpy()[18])

print(getPremioTotal(df))