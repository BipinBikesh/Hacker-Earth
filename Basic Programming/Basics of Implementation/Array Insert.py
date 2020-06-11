N,Q=list(map(int,input().split()))

arr=list(map(int,input().split()[:N]))

for i in range(Q):
    q1,a,b=list(map(int,input().split()))

    if (q1==1):
        arr[a]=b
    elif q1==2:
        if a>=0 and b<=len(arr):
            s=sum(arr[a:b+1])
            print(s)
        else:
            print(-1)
