T=int(input())
for i in range(T):
    s1,s2=list(map(str,input().split()))
    s1=list(s1)
    s2=list(s2)
    s1.sort()
    s2.sort()
    if s1==s2:
        print('YES')
    else:
        print('NO')
