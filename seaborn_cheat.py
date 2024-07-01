#%% dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pdb

#%% load the data
df = pd.read_csv('data_holder/titanic_dataset.csv')

#%% passing feature
data=df['Age']
#%%frequency distribution histogram
sns.displot(data) #counting occurance
sns.displot(data,stat='density') #here density
sns.displot(data, discrete=True) #does not combine bins
# to change bin width add binwidth=n in displot
# set fixed bin bins=n
#%% Kernel density distribution(kde)
sns.displot(data, kind='kde') #only kde density based
sns.displot(data, discrete = True, kde = True) #kde with histrogram count based

#%%Joint Distribution Plot
sns.jointplot(x = "Survived", y = "Age", data = df)
plt.show()
#%% basic count plot- use to count element
#Creating count plot
sns.catplot(x = 'Sex',hue="Pclass",kind="count",data=df,palette = "Blues")
# if see it in respect to categorial data then hue="feature_name"
#Adding the aesthetics
plt.title('Gender distribution')
plt.xlabel('category')
plt.ylabel('count') 
# Show the plot
plt.show()
#%% Heat map -compare ORDINAL data with feature
group = df.groupby(['Pclass', 'Survived'])
pclass_survived = group.size().unstack()

# Heatmap - Color encoded 2D representation of data.
sns.heatmap(pclass_survived, annot = True, fmt ="d")
#heatmap for missing value
#sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#%% Violinplot -Continuous Feature vs feature
# Violinplot Displays distribution of data
# across all levels of a category.
sns.violinplot(x ="Sex", y ="Age", hue ="Survived",
              data = df, split = True)

#%% Barplot
# Divide Fare into 4 bins
df['Fare_Range'] = pd.qcut(df['Fare'], 4)
 
# Barplot - Shows approximate values based
# on the height of bars.
sns.barplot(x ='Fare_Range', y ='Survived',data = df)

#%% box plot- to find outliers,average and more look on internet
sns.boxplot(x='Pclass',y='Age',data=df,palette='winter')