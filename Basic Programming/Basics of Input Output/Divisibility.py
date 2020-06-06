N=int(input())
arr=list(map(int,input().split()[:N]))
last_digit=[]
for i in range(N):
    last_digit.append(arr[i]%10)
new_num=0
for i in range(N):
    new_num=new_num*10+last_digit[i]
if new_num%10==0:
    print('Yes')
else:
    print('No')
