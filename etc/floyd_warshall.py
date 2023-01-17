INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

def print_all():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j]==INF:
                print("oo", end= " ")
            else:
                print(graph[i][j], end=" ")
        print()


for a in range(1, n+1):
    graph[a][a]=0

for _ in range(m):
    a, b, c =map(int, input().split())
    graph[a][b]=c

print_all()
for k in range(1, n+1):
    print()
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
    print_all()
