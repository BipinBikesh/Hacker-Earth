T=int(input())
lA=1
lB=7
for i in range(T):
    N=int(input())
    if N-lA<=lB-N:
        print('A')
        lA=N
    else:
        print('B')
        lB=N
    
