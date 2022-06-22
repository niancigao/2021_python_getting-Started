#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

april = np.array([271.5, 275.5, 283, 285, 283,

279.5, 278.5, 285, 287.5, 286.5,

306.5, 304, 295, 294, 295.5,

294, 298, 296.5, 299, 304.5])


stock=np.zeros(len(april)-1)
def diff(stock):                                          # A小題
    
    for i in np.arange(1,len(april)):
        stock[i-1]=np.array([april[i] - april[i-1]])

    print('平均數: ',np.mean(stock))
    print('中位數: ',np.percentile(stock,50))
    print('變異數: ',np.var(stock))
    print('標準差: ',np.std(stock))
    
diff(stock)


# In[ ]:




