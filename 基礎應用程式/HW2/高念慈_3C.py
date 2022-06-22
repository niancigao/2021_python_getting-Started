#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

april = np.array([271.5, 275.5, 283, 285, 283,

279.5, 278.5, 285, 287.5, 286.5,

306.5, 304, 295, 294, 295.5,

294, 298, 296.5, 299, 304.5])

march = np.array([311.0, 317.5, 320.5, 323.0, 315.0,

305.5, 307.0, 302.0, 294.0, 290.0,

276.5, 268.0, 260.0, 248.0, 270.0,

255.0, 267.5, 277.0, 280.0, 273.0,

267.5, 274.0])

stock=np.zeros(len(april)-1)
def diff(stock):                                          # A小題
    
    for i in np.arange(1,len(april)):
        stock[i-1]=np.array([april[i] - april[i-1]])

    #print('平均數: ',np.mean(stock))
    #print('中位數: ',np.percentile(stock,50))
    #print('變異數: ',np.var(stock))
    #print('標準差: ',np.std(stock))
    
diff(stock)

print('\n')

 
stock3 = np.zeros(len(march)-1)
def diff3(stock3):                                        # B小題
    
    for i in np.arange(1,len(march)):
        stock3[i-1]=np.array([march[i] - march[i-1]])
   
    #print('平均數: ',np.mean(stock3))
    #print('中位數: ',np.percentile(stock3,50))
    #print('變異數: ',np.var(stock3))
    #print('標準差: ',np.std(stock3))   
    
diff3(stock3)

print('\n')

#plt.subplot(211)                                          # C小題
plt.boxplot([stock,stock3])

plt.show


# In[ ]:




