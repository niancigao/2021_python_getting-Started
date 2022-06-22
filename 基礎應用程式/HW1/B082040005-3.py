#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = float(input('計算1至該正整數的合，請輸入一個正整數:'))

if (a%2==0 or a%2==1) and a>=0:
    a = int(a)
    sum = 0
    for b in range(1,a+1):
        sum= b + sum
        
    print(sum)

else:
    print('輸入錯誤')


# In[ ]:




