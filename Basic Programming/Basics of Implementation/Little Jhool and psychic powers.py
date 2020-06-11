binary=list(map(int,input()))
flag=0
for i in range(len(binary)-5):

    lst=binary[i:i+6]

    if(sum(lst)==0 or sum(lst)==6):

        flag=1
    else:
        continue

if(flag==1):
    print("Sorry, sorry!")
else:
    print('Good luck!')
