#!/usr/bin/env python
# coding: utf-8

# In[3]:


T=int(input())
toffee=0
for i in range(T):
    r,x=map(int,input().split())
    max_meter=100*x
    perimeter=2*(22/7)*r
    if(max_meter>=perimeter):
        toffee+=1
print(toffee)


# In[ ]:




