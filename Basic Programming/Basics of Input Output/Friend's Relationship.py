#!/usr/bin/env python
# coding: utf-8

# In[8]:


T=int(input())
for i in range(T):
    n=int(input())
    for j in range(1,n+1):
        print(('#'*(2*n-2*j)).center(2*n,'*'))


# In[ ]:




