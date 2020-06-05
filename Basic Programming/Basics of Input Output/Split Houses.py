n=int(input())
string=input()
a='YES'

for i in range(len(string)-1):
    if string[i]=='H'and string[i+1]=='H':
        a='NO'
        break
if a=='NO':
    print(a)
else:
    print(a)
    string=string.replace('.','B')
    print(string)
