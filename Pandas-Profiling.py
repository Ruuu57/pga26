#!/usr/bin/env python
# coding: utf-8

# Perform EDA In the Best Possible Way Using Pandas Profiling

# In[1]:


get_ipython().system('pip install numpy')


# In[2]:


pip install pandas-profiling==2.13.0 


# In[3]:


get_ipython().system('pip install ydata-profiling')
import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport # Use from ydata_profiling import ProfileReport


# In[4]:


from sklearn.datasets import load_diabetes


# In[5]:


diab_data=load_diabetes()


# In[6]:


df=pd.DataFrame(data=diab_data.data,columns=diab_data.feature_names)


# In[7]:


df.head()


# In[8]:


df.columns


# In[9]:


### To Create the Simple report quickly
profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)


# In[10]:


profile.to_widgets()


# In[11]:


profile.to_file("output.html")


# ##Titanic Dataset

# In[12]:


df=pd.read_csv('C:/Users/Ruuu/Downloads/titanic_data.csv')


# In[13]:


df.head()


# In[17]:


### To Create the Simple report quickly
profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)
profile


# In[15]:


profile.to_widgets()


# In[16]:


profile.to_file("output1.html")


# In[ ]:




