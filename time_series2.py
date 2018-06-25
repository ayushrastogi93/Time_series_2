# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 23:57:33 2018

@author: ilu-pc
"""
#time -series 2 
import pandas as pd 
import numpy as np
import datetime
dataset_raw = pd.read_csv("Train_SU63ISt.csv")
X = dataset_raw.iloc[:,1:2]
y = dataset_raw.iloc[:,2]
y[0] =8
# splitting dATA on dailybasis 
df = pd.read_csv("Train_SU63ISt.csv")
df['Count'][0] =8

for i in range(len(df['Datetime'])) :
    df['Datetime'][i] = "-".join(df['Datetime'][i].split(sep = "/"))
    date = datetime.datetime.strptime(df['Datetime'][i],'%d-%m-%Y %H:%M')                              
    df['Datetime'][i] = date.timetuple().tm_yday
    

    

print(y[0:24].sum())
print(y[24:48].sum())

X= df.iloc[0:5,1:2]
def split_date(date):
    s = "/".join(date.split(sep = "-") )
    return s
for j in range(len(X)):
  X['Datetime'][j] = split_date(X['Datetime'][j])
  date= datetime.datetime.strptime(X['Datetime'][j],'%d/%m/%Y %H:%M')                              
  X['Datetime'][j] = date.timetuple().tm_yday
