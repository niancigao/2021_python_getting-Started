#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

month = np.array([51655,52345,52677,56223,55318,56917,
                 58858,68559,69149,73236,80799,82568])
people = np.array([36343,34441,39164,36485,36204,43786,
                  49037,49472,50628,53438,62880,64510])

print(np.corrcoef(month,people))        #相關矩陣

coef = np.polyfit(month,people,1)       #A,B矩陣
reg_model = np.poly1d(coef)             #是數字 1 (1維度)
print(reg_model)  

plt.scatter(month,people)
plt.plot(month,reg_model(month),color='blue',label=reg_model) 

plt.title('Regression chart')
plt.xlabel('Salary')
plt.ylabel('Employees')     
plt.legend()     #圖例
plt.grid(True)   #格線

plt.show()


# In[ ]:




