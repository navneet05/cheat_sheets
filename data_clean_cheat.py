#%% dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pdb

#%%loading csv
df=pd.read_csv('data_holder/titanic_dataset.csv')
#%% getting familliar data 
print(df.info())
print(df.head())
print(df.describe())

#%%missing values
# droping whole feature depends on its importance when nan>40%
missValSum=df.isnull().sum() #type is series
#in percent
temp=missValSum.values/df.shape[0]*100 # return ndarray
missValPerc=[np.round(x,2) for x in temp]
indexVal=missValSum.index.tolist()
finalPer=pd.Series(dict(zip(indexVal,missValPerc)))
print(finalPer)
#short method
missing_values_per=(df.isnull().sum()/len(df)*100).round(2)
print(missing_values_per)


# %%
