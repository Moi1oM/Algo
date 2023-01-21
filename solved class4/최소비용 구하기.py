from heapq import heappush, heappop
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

frm, to = map(int, input().split())

distance = [INF] * (n+1)
distance[frm] = 0
q = []
heappush(q,(0,frm))

while q:
    dist, now = heappop(q)
    if distance[now] < dist:
        continue
    for city, cst in graph[now]:
        mid_cost = cst + dist
        if mid_cost < distance[city]:
            distance[city] = mid_cost
            heappush(q,(mid_cost, city))

print(distance[to])