from sys import stdin
from copy import deepcopy
sin = stdin.readline
res = 0
n = int(sin())
okay = []
for _ in range(n):
    l = list(map(int, sin().split()))
    okay.append(l)

ans = [0,0]
def track(row,col,cnt,color):
    global ans, n, l, r
    if col>=n:
        row += 1
        if col % 2 == 0:
            col = 1
        else:
            col = 0
    if row >= n:
        ans[color] = max(ans[color], cnt)
        return

    if okay[row][col] and not r[row+col] and not l[row-col]:
        r[row+col] = 1
        l[row-col] = 1
        track(row,col+2,cnt+1,color)
        r[row + col] = 0
        l[row - col] = 0
    track(row,col+2,cnt,color)


l = [0]*20
r = [0]*20

track(0,0,0,0)

track(0,1,0,1)

print(sum(ans))