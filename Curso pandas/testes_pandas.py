import pandas as pd
import numpy as np
from os import system

system('cls')
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s= 1
print(s)

traz as datas em um perido especificado
dates = pd.date_range('20231222', periods = 6)

df = pd.DataFrame(np.random(1, 4), index = dates, columns = list("ABCD"))
print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20231222"),
        "C": pd.Series(1, index = list(range(4)), dtype = "float32"),
        "D": np.array([3] * 4, dtype = "int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo"

    }
)

print(df2)
df2.sort_index(axis=1, ascending=False)
print(df2)

print(s.iloc[0])