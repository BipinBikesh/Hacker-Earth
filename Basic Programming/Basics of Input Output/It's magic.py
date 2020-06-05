n=int(input())
arr=list(map(int, input().split(' ')))
Sum=sum(arr)
lst=[]
for a in arr:
    if(Sum - a)%7==0:
        lst.append(a)
if len(lst)==0:
    print(-1)
else:
    print(arr.index(min(lst))) 
