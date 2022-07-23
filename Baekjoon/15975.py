n=int(input())
d=[[0] for _ in range(10001)]
maxidx=0
for _ in range(n):
    a,b=map(int,input().split())
    d[b].append(a)
    if maxidx<b:
        maxidx=b
for i in range(maxidx+1):
    d[i].sort()
res=0
for i in range(1,maxidx+1):
    if len(d[i]) == 1 or len(d[i])==2:
        continue
    for j in range(1,len(d[i])):
        if j==1:
            tmp=d[i][2]-d[i][1]
        elif j==len(d[i])-1:
            tmp=d[i][j]-d[i][j-1]
        else:
            tmp=min(d[i][j]-d[i][j-1],d[i][j+1]-d[i][j])
        res+=tmp
print(res)