a=input()
a=a.lower()
d=[0]*26
for i in a:
    alpha=int(ord(i))-int(ord('a'))
    d[alpha]+=1
max=0
for i in d:
    if max<i:
        max=i
index=-1
check=0
ch=1
for i in range(len(d)):
    if d[i]==max:
        if check==1:
            ch=1
            break
        index=i
        check=1
if ch==0:
    print()