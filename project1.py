#!/usr/bin/env python
# coding: utf-8

# # Pubg - DS Project

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Task - 1: Reading the datase

# In[3]:


ds = pd.read_csv("C:\\Users\\balaj\\Downloads\\datas.csv")
ds


# # Task - 2: Check the datatype of all the columns.

# In[16]:


data_type = ds.dtypes
data_type


# # Task - 3:Find the summary of all the numerical columns and write your findings about it

# In[17]:


summary = ds.describe()
summary


# # Task - 4:The average person kills how many players?

# In[18]:


avg = ds['kills'].mean()
print("\nThe average person kills :", avg,"player")


# # Task - 5: how many kills do 99% of people have?

# In[19]:


no = ds["kills"].quantile(0.99)
print("\n99% of people have",no,"kills")


# # Task - 6: The most kills ever recorded are how much?

# In[20]:


most_kill = ds["kills"].max()
print("\nThe most kill ever recorded are :",most_kill)


# # Task - 7: Print all the columns of the dataframe.

# In[21]:


ds.columns


# # Task - 8: Comment on distribution of the match's duration. Use seaborn.

# In[22]:


sns.distplot(ds['matchDuration'])


# # Task - 9: Comment on distribution of the walk distance. Use seaborn.

# In[23]:


sns.distplot(ds['walkDistance']);


# # Task - 10: Plot distribution of the match's duration vs walk distance one below the other.

# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('classic')
plt.figure()
# ploting matchDuration
plt.subplot(2,1,1)
plt.plot(ds["matchDuration"],"-")
plt.xlabel("Match Duration")
# ploting walkDistance
plt.subplot(2,1,2)
plt.plot(ds["walkDistance"],"--")
plt.xlabel("Walk Distance")


# # Task - 11: Plot distribution of the match's duration vs walk distance side by side.

# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('classic')
plt.figure(figsize=(10,5))

# ploting matchDuration
plt.subplot(1,2,1)
plt.plot(ds["matchDuration"])
plt.xlabel("Match Duration:")

# ploting walkDistance
plt.subplot(1,2,2)
plt.plot(ds["walkDistance"])
plt.xlabel("Walk Distance:")


# # Task - 12: Pairplot the dataframe. Comment on kills vs damage dealt, Comment on maxPlace vs numGroups

# In[4]:


sns.pairplot(ds.head(700));


# # Task - 13: How many unique values are there in 'matchType' and their counts?

# In[7]:


a = pd.unique(ds['matchType'])
print("\nUnique value in matchType is :",a)
b = len(a)
print("\nCount of unique value in matchType is :",b)


# # Task - 14:Plot a barplot of ‘matchType’ vs 'killPoints'. Write your inferences.

# In[5]:


sns.barplot(ds['matchType'],ds['killPoints']);


# # Task - 15: Plot a barplot of ‘matchType’ vs ‘weaponsAcquired’. Write your inferences.

# In[6]:


sns.barplot(ds['matchType'],ds['weaponsAcquired']);


# # Task - 16: Find the Categorical columns.

# In[8]:


category_col = ds.select_dtypes('category').columns 
category_col


# # Task - 17: Plot a boxplot of ‘matchType’ vs ‘winPlacePerc’.

# In[9]:


sns.boxplot(x='matchType', y='winPlacePerc', data=ds);


# # Task - 18: Plot a boxplot of ‘matchType’ vs ‘matchDuration’. 

# In[10]:


sns.boxplot(x='matchType', y='matchDuration', data=ds);


# # Task - 19: Change the orientation of the above plot to horizontal.

# In[11]:


sns.boxplot( x='matchDuration', y='matchType',data=ds);


# # Task - 20: Add a new column called ‘KILLABLES’ which contains the sum of following columns viz. headshotKills, teamKills, roadKills.

# In[16]:


ds['KILLABLES'] = ds['headshotKills'] + ds['teamKills'] + ds['roadKills']
ds['KILLABLES']


# # Task - 21: Round off column ‘winPlacePerc’ to 2 decimals.

# In[13]:


ds['winPlacePerc'].round(decimals=2)


# # Task - 22: Take a sample of size 50 from the column damageDealt for 100 times and calculate its mean. Plot it on a histogram.

# In[15]:


mean = []
for i in range(100):
  for x in range(0,1001,50):
    mean1 = ds['damageDealt'].head(x).mean()
    mean.append(mean1)
sns.histplot(data=ds['damageDealt'], x=mean)


# In[ ]:


#--------------------------------------------------------------------------------------

