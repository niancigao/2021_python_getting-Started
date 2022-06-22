#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
data = datasets.load_diabetes().data
target = datasets.load_diabetes().target


from sklearn.model_selection import train_test_split #分割資料集的函式
data_train, data_test, target_train, target_test = train_test_split(data,target,test_size=0.2)


from sklearn.linear_model import LinearRegression
#匯入scikit-learn的線性回歸模型
regr_model = LinearRegression()          #建立模型物件
regr_model.fit(data_train,target_train)  #放訓練!!     #用訓練集來訓練模型


#決定係數(coefficient of determination)
print(regr_model.score(data_train,target_train).round(3)) #訓練集
print(regr_model.score(data_test,target_test).round(3))   #測試集


#殘差圖
import numpy as np
import matplotlib.pyplot as plt

predictions = regr_model.predict(data_test) 

x = np.arange(predictions.size)
y = x*0                                       #數量一樣才能畫圖
              
plt.scatter(x,predictions-target_test)
plt.plot(x,y,color='yellow')
plt.show()


# In[ ]:




