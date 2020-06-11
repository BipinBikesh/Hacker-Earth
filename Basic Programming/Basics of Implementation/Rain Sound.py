#rain sound
import math
T=int(input())
for i in range(T):
    lrs=list(map(int,input().split()))
    l=math.ceil(lrs[0]/lrs[2])
    r=math.floor(lrs[1]/lrs[2])
    if l>r:
        print("-1 -1")
    else:
        print(str(l)+" "+str(r))
