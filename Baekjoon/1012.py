import sys
n = int(sys.stdin.readline())
m = 0
gd=[]
def f(x, y):
    global gd
    global m
    global n
    global visited
    if x<0 or y<0 or x>=m or y>=n:
        return 0
    elif gd[x][y] == 0:
        return 0
    else:
        visited[x][y] = True
        if not visited[x-1][y]:
            f(x-1,y)
        if not visited[x+1][y]:
            f(x+1,y)
        if not visited[x][y-1]:
            f(x,y-1)
        if not visited[x][y+1]:
            f(x,y+1)

visited=[]
for _ in range(n):
    cnt=0
    gd=[[0]*51 for _ in range(51)]
    m, n, k = map(int, sys.stdin.readline().split())
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        gd[x][y]=1
    visited = [[False]*51 for _ in range(51)]
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and gd[i][j] == 1:
                f(i,j)
                cnt+=1
    print(cnt)