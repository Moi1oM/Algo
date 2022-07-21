d=[]
n=int(input())
d=[-1]*(n+2)
d[0]=0
d[1]=1
d[2]=1
if n<=2:
    print(d[n])
else:
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
    print(d[n])