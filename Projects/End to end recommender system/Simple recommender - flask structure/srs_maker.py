import pandas as pd
import numpy as np
import os
import flask
import pickle

df_merged = pd.read_pickle("./df_merged.pkl")

###Improving srs_model function


def srs_model(percentage):
    percentage = float(percentage)
    emp_arr = []
    name_arr = []
    for i in df_merged['Name']:
    
        V = df_merged[df_merged['Name'] == str(i)]['Count']
        M = df_merged['Count'].quantile(percentage)
        R =  df_merged[df_merged['Name'] == str(i) ]['Rating']
        C = df_merged['Rating'].mean()

        WR = ((V/(V+M))*R) + ((M/(V+M)) * C)
        
        emp_arr.append(WR.values[0])
        name_arr.append(i)
    zip1 = zip(name_arr, emp_arr)
    df_new = pd.DataFrame(zip1, columns = ['name', 'rating'])
    df_new = df_new.sort_values(by = 'rating', ascending = False)
    return df_new #Add a sort function to this model