import sys
from collections import deque
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip())
d = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    d[a].append(b)
    d[b].append(a)
#print(d)
que = deque()
que.append(1)
res = [0]*(n+1)


def f(num,parent):
    global que, d, res
    if len(d[num])==0:
        return 0
    res[num]=parent
#    print(num,parent,res)
    d[num].remove(parent)
    for i in range(len(d[num])):
        f(d[num][i], num)
    return 0

while que:
    x = que.popleft()
    for j in range(len(d[x])):
        f(d[x][j], x)
#print(res)
for i in range(2,n+1):
    print(res[i])