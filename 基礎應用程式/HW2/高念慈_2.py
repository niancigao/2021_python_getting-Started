#!/usr/bin/env python
# coding: utf-8

# In[3]:


def calculator(x = 8, z = '', y = 9):
    
    if z == '+' :
        print(x+y)
    elif z == '-' :
        print(x-y)
    elif z == '*' :
        print(x*y)
    elif z == '/' :
        if y!=0:
            print(x/y)
        else:
            print('False')

calculator(8,'+',9)
calculator(8,'-',9)
calculator(8,'*',9)
calculator(8,'/',9)


# In[ ]:




