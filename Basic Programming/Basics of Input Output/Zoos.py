#!/usr/bin/env python
# coding: utf-8

# In[ ]:


string=input()
y=0
x=0
for i in range(len(string)):
    if string[i]=='z':
        x+=1
    elif string[i]=='o':
        y+=1
if 2*x==y:
    print('Yes')
else:
    print('No')


# In[ ]:




