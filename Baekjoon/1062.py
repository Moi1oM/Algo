from itertools import combinations
arr=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#print(list(combinations(arr,3)))
n,k=map(int,input().split())
#print(list(combinations(arr,k)))
alphamap=[]
maxalpha=0
for _ in range(n):
    a=input()
    d=[0]*26
    s=[]
    for i in range(len(a)):
        alpha=int(ord(a[i]))-int(ord('a'))
        d[alpha]=1
    for i in range(len(d)):
        if i!=0 and i!=2 and i!=8 and i!=13 and i!=19:
            s.append(d[i])
    if maxalpha<sum(d):
        maxalpha=sum(d)
    alphamap.append(s)
if maxalpha<=k:
    print(n)
elif k<5:
    print(0)
#else:

print(alphamap)
print(maxalpha)