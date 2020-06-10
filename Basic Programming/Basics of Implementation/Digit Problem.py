xk = list(input().split())

x = list(xk[0])

k = int(xk[1]) 

for i in range(len(x)):

    if x[i]!='9' and k>0:

        x[i]='9'

        k-=1

res = int("".join(x))

print(res)
