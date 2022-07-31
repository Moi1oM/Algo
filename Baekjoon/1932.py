n = int(input())
graph = [[0]*n for _ in range(n)]
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(len(a)):
        graph[i][j] = a[j]


def f(x,y):
    if y == 0:
        graph[x][y] += graph[x-1][y]
    else:
        nx1 = x - 1
        ny1 = y
        nx2 = x - 1
        ny2 = y - 1
        graph[x][y] = max(graph[x][y]+graph[nx1][ny1], graph[x][y]+graph[nx2][ny2])

for i in range(1,n):
    for j in range(i+1):
        f(i,j)
print(max(graph[n-1]))