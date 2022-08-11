#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 16:29:26 2021


import pandas as pd
file_data= '/Users/sahilbhat/Downloads/Task2_Expenses_by_client.csv'
df_data= pd.read_csv(file_data)
print(df_data)
df_data= df_data.drop(columns=df_data.columns[0])
df_data_group= df_data.groupby('name',as_index=False)['expenses'].mean()
print(df_data_group)
min_expense=min(df_data_group['expenses'])
print(min_expense)
minimum_expense=df_data_group[df_data_group['expenses']==min_expense]
print(minimum_expense)
a=minimum_expense.values.tolist()
print(a[0])

df_data_total=df_data.groupby('name',as_index=False)['expenses'].sum()
#print(df_data_total)
maxx_expense=max(df_data_total['expenses'])
df_data_max_expense=df_data_total[df_data_total['expenses']==maxx_expense]
df_data_max_expense1=df_data_max_expense.drop('expenses', axis=1)
print(df_data_max_expense1)
b=df_data_max_expense1.values.tolist()
print(b[0])




























