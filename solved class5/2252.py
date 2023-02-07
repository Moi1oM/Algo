from collections import deque
from sys import stdin
sin = stdin.readline

n,m = map(int, sin().split())
ind = [0]*(n+1)
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sin().split())
    g[a].append(b)
    ind[b]+=1

result = []
q = deque()
for i in range(1,n+1):
    if ind[i]==0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for v in g[now]:
        ind[v]-=1
        if ind[v]==0:
            q.append(v)

for val in result:
    print(val,end=" ")