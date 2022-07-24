n=int(input())
IN=[]
maxnum=0
for _ in range(n):
    a=int(input())
    IN.append(a)
    if maxnum<a:
        maxnum=a
d=[0]*(maxnum+1)
d[1]=1
d[2]=2
d[3]=4
if maxnum>=4:
    for i in range(4,maxnum+1):
        d[i]=d[i-1]+d[i-2]+d[i-3]
for i in IN:
    print(d[i])