# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:12:29 2021

@author: u27d09
"""
#%% dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%% data
df=pd.read_csv('data_holder/titanic_dataset.csv')
#%% line plot
xpoint=np.array([0,3,4,5])
ypoint=np.array([0,15,20,25])
plt.plot(xpoint,ypoint,marker='o',color='red',mec='green',ms=15) #default is line,only pass 'o' for rings in place of line
# if we don't give any axis then for that default will be 0 to length of other axis
# marker to highlight point, ms for size mec for edge color, mfc-inside color of marker
# ls-for line style lw-line width
#plt.plot(xpoint) #for multiple line
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('show you something')
plt.grid()
plt.show()
#%% multiple plot in single figure
xpoint=np.array([0,3,4,5,7,9])
ypoint=np.array([0,15,20,25,35,45])
#plot 1:
plt.subplot(2,2,1) #1-row 2-column 3-its position
plt.plot(xpoint,ypoint,marker='o',color='red',mec='green',ms=15)
# plot 2:
ypoint=np.array([0,18,40,45,35,45])
plt.subplot(2,2,2)
plt.plot(xpoint,ypoint,marker='o',color='yellow',mec='green',ms=15)
#plot 3:
x=np.array([1,2,3,4])
y=np.array([1,4,6,8])
plt.subplot(2,2,3)
plt.plot(x,y)
plt.suptitle('whole figure title')
plt.show()
#%% scatter plot
x=np.array([1,2,3,4])
y=np.array([1,4,6,8])
plt.scatter(x, y)
#compare two scatter plot
x=np.array([1,2,3,4])
y=np.array([1,6,9,12])
plt.scatter(x, y,color='green')
plt.show()
#%% bar graphs
x=np.array(['A','B','C','D'])
y=np.array([1,4,6,8])
plt.bar(x, y,color='green',width=0.4) #barh for horizontal bar

#%% histrogram
plt.hist(df['Age'], 
         facecolor='green', 
         edgecolor='blue', 
         bins=20)
plt.show()
#%% components of histrogram
n, bins, patches = plt.hist(df['Age'], 
                            facecolor='green', 
                            edgecolor='blue', 
                            bins=20)
# if cumulitive=True then it add bins and last show total
# if range(a,b) show olny this range
print('n: ', n) #Contains the frequency of each bin
print('bins: ', bins) #Represents the middle value of each bin
print('patches: ', patches) #The Patch object for the rectangle shape representing each bar