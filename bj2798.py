N,M=map(int,input().split())
d=list(map(int,input().split()))
MAX=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            num=d[i]+d[j]+d[k]
            if num>M:
                continue
            elif MAX<num:
                MAX=num
print(MAX)