N,Q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(Q):
    L,R=map(int,input().split())
    subarray=arr[L-1:R]
    length=R-(L-1)
    sum=0
    for i in subarray:
        sum+=i
    res=sum//length
    print(res)
