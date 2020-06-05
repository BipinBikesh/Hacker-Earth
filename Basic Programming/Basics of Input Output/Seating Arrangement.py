#!/usr/bin/env python
# coding: utf-8

# In[ ]:


T=int(input())
for i in range(T):
    N=int(input())
    seat=N%12
    if seat==0:
        seat_facing=N-11
        seat_type='WS'
    elif seat==1:
        seat_facing=N+11
        seat_type='WS'
    elif seat==2:
        seat_facing=N+9
        seat_type='MS'
    elif seat==3:
        seat_facing=N+7
        seat_type='AS'
    elif seat==4:
        seat_facing=N+5
        seat_type='AS'
    elif seat==5:
        seat_facing=N+3
        seat_type='MS'
    elif seat==6:
        seat_facing=N+1
        seat_type='WS'
    elif seat==7:
        seat_facing=N-1
        seat_type='WS'
    elif seat==8:
        seat_facing=N-3
        seat_type='MS'
    elif seat==9:
        seat_facing=N-5
        seat_type='AS'
    elif seat==10:
        seat_facing=N-7
        seat_type='AS'
    else:
        seat_facing=N-9
        seat_type='MS'
    print(seat_facing, seat_type)

    


# In[ ]:


1
4
6
88
44
44
44

