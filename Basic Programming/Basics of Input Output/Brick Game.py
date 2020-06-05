n=int(input())
c=0
c1=0.0
for i in range(1,n+1):
    c+=i
    if(c+c1>=n):
        print('Patlu')
        break
    c1+=i*2
    if(c+c1>=n):
        print('Motu')
        break
