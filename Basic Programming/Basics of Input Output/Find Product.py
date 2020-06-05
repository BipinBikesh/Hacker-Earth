n=int(input())
lst=list(map(int,input().split()[:n]))
answer=1
for i in range(len(lst)):
    answer=(answer*lst[i])%(10**9+7)
print(answer)
