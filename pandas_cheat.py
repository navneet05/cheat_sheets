#%% dependencies
import pandas as pd

#%%series
calories = {"day1": 420, "day2": 380, "day3": 390}
mydfa = pd.Series(calories) #key will became label
print(mydfa) # if no lable default index became lable
# .index for keys

# %%making dataframe
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"], 
  'passings': [3, 7, 2]
}
mydf = pd.DataFrame(mydataset) #one more arg can pass-index=[values,]
print(mydf)

#%%show data
print(mydf[:1]) #direct
print(mydf.loc[0]) #by row index result is series
print(mydf.loc[[0,1]]) #with range result is dataframe
print(mydf.head(10)) #top element default 5
print(mydf.tail()) #last element default 5

#%%load  csv file
df=pd.read_csv('data_holder/titanic_dataset.csv')
print(df[:5]) # .to_string() to print entire dataframe

#%%load json file
dfa=pd.read_json('data.js')

#%% show mathametical describtion
print(df.describe()) 

#%% tell about data
print(dfa.info()) 

#%%see whole file
print(dfa.to_string()) 

#%%give columns in numpy array to convert in list .tolist()
a=df.columns.values 

#%%gives missing value count columnwise
print(df.isnull().sum()) 

#%%show no. of row and column
print(df.shape) # in tuple

#%%unique elements in column 
print(df[a[1]].value_counts().size)

#%%column values count
print(len(df.loc[df.Sex=="male"].index))
print(len(df.loc[df.Sex=="female"].index))

#%% group by- to analyze category data
df_groupby_sex = df.groupby('Sex')
temp_group=df_groupby_sex.ngroups 
# .groups to get row number of same group
# .size() to get size
# .get_group(group_name) to get particular group 

#%% Agregation function
maxAge=df.groupby('Sex').Age.max()
# if want to find category max then use above
# multiple agg then
holder=df.groupby('Sex').Age.agg(['max', 'min', 'count', 'median', 'mean'])