from sys import stdin

sin = stdin.readline

n, m = map(int, sin().split())
parent = [i for i in range(n)]
g = []
for _ in range(m):
    n1, n2 = map(int, sin().split())
    g.append((n1,n2))

def find_p(x):
    if parent[x]==x:
        return x
    else:
        parent[x] = find_p(parent[x])
        return parent[x]

def union_p(a,b):
    aa = find_p(a)
    bb = find_p(b)
    if aa < bb:
        parent[bb] = aa
    else:
        parent[aa] = bb

res = 0
for i in range(m):
    n1, n2 = g[i][0], g[i][1]
    if find_p(n1) == find_p(n2):
        res = i+1
        break
    else:
        union_p(n1,n2)
#print(parent)
print(res)