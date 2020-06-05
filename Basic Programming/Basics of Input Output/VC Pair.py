#!/usr/bin/env python
# coding: utf-8

# In[10]:


T=int(input())
vol=['a','e','i','o','u']

for i in range(T):
    N=int(input())
    s=input()[:N]
    count=0
    for i in range(N-1):
        if s[i] not in vol and s[i+1] in vol:
            count+=1
    print(count)


# In[ ]:




