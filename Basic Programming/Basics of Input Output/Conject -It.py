T=int(input())
for i in range(T):
    n=int(input())
    while(n>=1):
        if n==1:
            print('YES')
            break
        else:
            if n%2==0:
                n=n//2
            else:
                n=3*n+1
    if n<1:
        print('NO')
                
