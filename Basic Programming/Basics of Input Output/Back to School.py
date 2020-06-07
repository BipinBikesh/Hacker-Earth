n1,n2,n3=map(int,input().split())
if n1>=n2 and n1>=n3:
    maxi=n1
elif n2>=n1 and n2>=n3:
    maxi=n2
else:
    maxi=n3
    
print(maxi)
##
##or you can use this one liner
##
##print(max(list(map(int,input().split()))))
