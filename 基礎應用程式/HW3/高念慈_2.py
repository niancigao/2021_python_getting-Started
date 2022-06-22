#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Microsoft JhengHei'  #(微軟正黑體) 

df = pd.DataFrame(pd.read_csv(r'C:\Users\user\Downloads\HW3_2.csv' ))
print('男生計: ',sum(df['男生計'])) 
print('女生計: ',sum(df['女生計']))


df_cols=df[['男生計','女生計']]
sns.pairplot(df_cols, kind = 'reg', height = 4, diag_kws = dict(bins = 10))
sns.set_style("ticks")

plt.show()


# In[ ]:




