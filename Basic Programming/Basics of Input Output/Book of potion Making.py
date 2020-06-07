isbn=input()
sum=0
if len(isbn)!=10:
    print('Illegal ISBN')
else:
    for i in range(len(isbn)):
        sum+=int(isbn[i])*(i+1)
    if sum%11==0:
        print('Legal ISBN')
    else:
        print('Illegal ISBN')
