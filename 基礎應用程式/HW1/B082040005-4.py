#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

point={1:'1 point',
       2:'2 point',
       3:'3 point',
       4:'4 point',
       5:'5 point',
       6:'6 point',
       7:'7 point',
       8:'8 point',
       9:'9 point',
       10:'10 point',
       11:'Jack',
       12:'Queen',
       13:'king'}

color={'a':'黑桃', 'b':'愛心', 'c':'菱形', 'd':'梅花'}

flower=random.choice('abcd')
dice=random.randint(1,13)

print("花色、點數:")
print(color[flower],point[dice])


# In[ ]:




