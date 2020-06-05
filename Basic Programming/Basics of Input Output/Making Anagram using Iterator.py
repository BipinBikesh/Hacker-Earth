from collections import Counter
T=int(input())
for i in range(T):   
    a=Counter(input())
    print(a)
    b=Counter(input())
    print(b)
    c=a-b
    print(c)
    d=b-a
    print(d)
    e=c+d
    print(e)
    print(list(e.elements()))
    print(len(list(e.elements())))
