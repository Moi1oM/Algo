n = int(input())
graph = []
visited = [[False]* n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input())))
dx = [0,0,-1,1]
dy = [-1,1,0,0]
res = []

def bfs(x,y,idx):
    visited[x][y]=True
    graph[x][y]=idx
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            bfs(nx,ny,idx)
    return 0

index = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
                index += 1
                bfs(i,j,index)
print(index-1)
res = [0]*(index+1)
for i in range(2,index+1):
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] == i:
                cnt += 1
    res[i] = cnt
res.sort()
for i in range(2,index+1):
    print(res[i])