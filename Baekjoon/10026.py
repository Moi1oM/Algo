import sys
sys.setrecursionlimit(10**6)

def non(x, y, color):
    global rgb, n, visited
    if visited[x][y]:
        return 0

    visited[x][y] = True
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        ddx = dx[i] + x
        ddy = dy[i] + y
        if ddx < 0 or ddx >= n or ddy < 0 or ddy >= n:
            continue
        elif visited[ddx][ddy]:
            continue
        elif color == rgb[ddx][ddy]:
            non(ddx, ddy, color)
    return 0


def on(x, y, color):
    global rgb, n, visited
    if visited[x][y]:
        return 0
    visited[x][y] = True
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        ddx = dx[i] + x
        ddy = dy[i] + y
        if ddx < 0 or ddx >= n or ddy < 0 or ddy >= n:
            continue
        elif visited[ddx][ddy]:
            continue
        elif color == 'R' or color == 'G':
            if rgb[ddx][ddy] == 'R' or rgb[ddx][ddy] == 'G':
                on(ddx, ddy, color)
        else:
            if rgb[ddx][ddy] == 'B':
                on(ddx, ddy, color)
    return 0


n = int(sys.stdin.readline())
rgb = []
for _ in range(n):
    rgb.append(sys.stdin.readline())
visited = [[False] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            non(i, j, rgb[i][j])
            cnt += 1
a = cnt
cnt = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            on(i, j, rgb[i][j])
            cnt += 1
b = cnt
print(a, b)
