T=int(input())
for i in range(T):
    ab=list(input().split())
    a=int(ab[0])
    b=int(ab[1])
    r1=a//b
    r2=b//a
    res=max(r1,r2)
    print(res)
