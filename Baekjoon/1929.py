import math

m,n=map(int,input().split())
d=[True]*(n+1)
d[0]=False
d[1]=False
for i in range(2,int(math.sqrt(n)+1)):
    for j in range(i*2,n+1,i):
        d[j] = False
for i in range(m,n+1):
    if d[i]:
        print(i)