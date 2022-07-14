n,m=map(int, input().split())
d=[]
for i in range(n):
    data=list(map(int, input().split()))
    MIN=min(data)
    d.append(MIN)
print(max(d))