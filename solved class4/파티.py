n,m,x = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
for _ in range(m):
    a, b, c =map(int, input().split())
    graph[a][b]=c

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j]= min(graph[i][j],graph[i][k]+graph[k][j])

res = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j], end=" ")
    print()

for i in range(1, n+1):
    cost = graph[i][x]+graph[x][i]
    if res < cost:
        res = cost

print(res)