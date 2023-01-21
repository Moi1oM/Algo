n,m,r = map(int, input().split())
items = list(map(int, input().split()))
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, c =map(int, input().split())
    graph[a][b]=c
    graph[b][a]=c

for i in range(1,n+1):
    graph[i][i]=0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
res = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if m >= graph[i][j]:
            cnt+=items[j-1]
    if res < cnt:
        res = cnt
print(res)
