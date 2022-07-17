a=int(input())
b=int(input())
c=int(input())
mul=a*b*c
d=[0]*10
while mul>0:
    index=mul%10
    d[index]+=1
    mul=mul//10
for i in d:
    print(i)