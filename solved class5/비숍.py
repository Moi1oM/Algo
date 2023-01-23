from sys import stdin
from copy import deepcopy
sin = stdin.readline
res = 0
n = int(sin())
okay = []
for _ in range(n):
    a = []
    l = list(map(int, sin().split()))
    for i in l:
        if i == 0:
            a.append(False)
        if i == 1:
            a.append(True)
    okay.append(a)

def make_false(g,a,b):
    dx = [-1, -1, 1, 1]
    dy = [1, -1 ,1, -1]
    g[a][b]=False
    for i in range(4):
        nx = a
        ny = b
        while True:
            nx = nx + dx[i]
            ny = ny + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break
            g[nx][ny] = False
    return
def is_full(grp):
    rtn = True
    for i in range(n):
        for j in range(n):
            if grp[i][j]==True:
                rtn = False
    return rtn

def print_g(g):
    for i in range(n):
        for j in range(n):
            print(g[i][j], end=" ")
        print()
    print()

def bishop(g, k):
    global res
    if is_full(g):
        #print(k)
        if k > res:
            res = k
        return

    for i in range(n):
        for j in range(n):
            if g[i][j]:
                #print(i,j,k)
                gg = deepcopy(g)
                make_false(gg,i,j)
                bishop(gg,k+1)

for i in range(n):
    for j in range(n):
        if okay[i][j]:
            #print(i,j)
            graph = deepcopy(okay)
            make_false(graph,i,j)
            #print_g(graph)
            bishop(graph, 1)

print(res)