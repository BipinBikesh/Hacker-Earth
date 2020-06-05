##T=int(input())
##for i in range(T):
##    grn_cst,pur_cst=map(int,input().split())
##    n=int(input())
##    min_cst=0
##    for x in range(n):
##        j,k=map(int,input().split())
##        min_cst+=min(j*grn_cst+k*pur_cst,j*pur_cst+k*grn_cst)
##    print(min_cst)
t=int(input())
for i in range(t):
    grn_cst,pur_cst=map(int,input().split())
    n=int(input())
    min_cst=0
    lst1=[]
    lst2=[]
    for x in range(n):
        j,k=map(int,input().split())
        lst1.append(j)
        lst2.append(k)
    
    count_j=lst1.count(1)
    count_k=lst2.count(1)
    min_cst=min(count_j,count_k)*max(grn_cst,pur_cst)+max(count_j,count_k)*min(grn_cst,pur_cst)
    print(min_cst)
