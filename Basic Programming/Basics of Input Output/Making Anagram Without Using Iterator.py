count1=[0]*26
count2=[0]*26
str1=input()
str2=input()

for i in range(0,len(str1)):
    count1[ord(str1[i])-ord('a')]+=1
for i in range(0,len(str2)):
    count2[ord(str2[i])-ord('a')]+=1
res=0
for i in range(26):
    res+=abs(count1[i]-count2[i])

print(res)
