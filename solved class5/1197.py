from sys import stdin
from heapq import heappush, heappop
sin = stdin.readline

v, e = map(int, sin().split())
q = []
for _ in range(e):
    a, b, c = map(int, sin().split())
    heappush(q,(c,a,b))

parent = [i for i in range(v+1)]

def find_p(x):
    global parent
    if parent[x]==x:
        return x
    else:
        parent[x] = find_p(parent[x])
        return parent[x]

def union_p(x, y):
    global parent
    a = find_p(x)
    b = find_p(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

res = 0
while q:
    cost, frm, to = heappop(q)
    if find_p(frm) != find_p(to):
        union_p(frm, to)
        res += cost
print(res)