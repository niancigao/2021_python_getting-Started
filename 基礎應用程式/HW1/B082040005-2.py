#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = float(input('請輸入購買金額:'))

if a>=100000 and (a%2==0 or a%2==1):
    a = a*0.8
    print('打八折:',round(a))
elif 100000>a>=50000 and (a%2==0 or a%2==1):
    a = a*0.85
    print('打八五折:',round(a))
elif 50000>a>=30000 and (a%2==0 or a%2==1):
    a = a*0.9
    print('打九折:',round(a))
elif 30000>a>=10000 and (a%2==0 or a%2==1):
    a = a*0.95
    print('打九五折:',round(a))
elif 10000>a>=0 and (a%2==0 or a%2==1):
    print('不折扣:',round(a))
else:
    print('輸入錯誤')


# In[ ]:




