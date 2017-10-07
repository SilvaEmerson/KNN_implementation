#-*- coding:utf-8 -*-

import pandas as pd
import KNN

df = pd.read_csv('data/data.txt')
#df.drop(1,axis=1,inplace=True)
print(df)
df = df.values.tolist()
print(df)