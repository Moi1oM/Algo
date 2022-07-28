import sys
n,m=map(int, sys.stdin.readline().split())
d=list(map(int,sys.stdin.readline().split()))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    cnt=0
    for i in range(a,b+1):
        cnt+=d[i-1]
    print(cnt)