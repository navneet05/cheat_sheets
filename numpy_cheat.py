#%% dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% basic array
arr=np.array([1,2,3,4,5,6,7,8])
arr1=np.array([[1,2],[3,4]]) #2d
arr3=np.array([1,2,3])
arr4=np.array([4,5,6])
print(arr) #and by index also start from 0 and negative index also be use

#%% zero array
a=np.zeros(shape=(10))

#%% check dimension
print(arr.ndim)

#%% check array datatype 
print(arr.dtype)

#%% fetching particular elements
print(arr[1:4]) # exclude last
print(arr[1:])  # to the last

#%% slicing steps
print(arr[:7:2])

#%% slicing 2d array
print(arr1[1,1:])

#%% copy array
x=arr.copy()

#%% size
print(arr.shape)

#%% reshape array
newarr=arr.reshape(4,2) # 1d to 2d and its view
print(newarr)

#%% iterating 2d
for x in np.nditer(arr1):
	print(x)

#%% iteration with datatype change
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
	print(x)

#%% join 2 array
newarr3=np.concatenate((arr3,arr4))
print(newarr3)

#%% search
y=np.where(arr4==4)

#%%sort
print(np.sort(arr3)) #gives copy of array

#%% filter
temp=[True,False,False]
temp1=arr3[temp]
print(temp1)
# %%
