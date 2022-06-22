#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests

iss= requests.get('http://api.open-notify.org/iss-now.json')

#iss.json() 先存成字典 再抓資料

#print(iss.json()['iss_position'])  字典中再取字典

print('國際太空站位置: ',iss.json()['iss_position']['latitude'],iss.json()['iss_position']['longitude'])


# In[ ]:




