from sys import stdin
from heapq import heappush, heappop

sin = stdin.readline

n, m = map(int, sin().split())
INF = int(1e8)
g = [[] for _ in range(n+1)]

for _ in range(m):
    f, t, c = map(int, sin().split())
    g[f].append((t,c))
    g[t].append((f,c))
    # g[f][t] = c
    # g[t][f] = c

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heappush(q,(0,start))

    while q:
        mid_cost, now = heappop(q)
        if mid_cost > distance[now]:
            continue
        for to, cost in g[now]:
            if distance[to] > cost+mid_cost:
                distance[to] = cost+mid_cost
                heappush(q,(mid_cost+cost,to))
    return distance
arr1 = dijkstra(1)

# for k in range(1,n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             g[a][b] = min(g[a][b],g[a][k]+g[k][b])
#
u1, u2 = map(int, sin().split())
arr2 = dijkstra(u1)
arr3 = dijkstra(u2)
d1 = arr1[u1]+arr2[u2]+arr3[n]
d2 = arr1[u2]+arr3[u1]+arr2[n]
res = min(d1,d2)
if res >= INF:
    print(-1)
else:
    print(res)

#
# print(min(g[1][u1]+g[u1][u2]+g[u2][n],g[1][u2]+g[u2][u1]+g[u1][n]))


