from heapq import heappush, heappop

v, e = map(int, input().split())
start = int(input())
mapping = [[] for _ in range(v+1)]
visited = [False] * (v+1)
for _ in range(e):
    sn, en, cost = map(int, input().split())
    mapping[sn].append((en, cost))

INF = int(1e9)
costs = [INF] * (v+1)
costs[start] = 0
visited[start] = True

q = []
heappush(q,(0,start))

while q:
    c, n = heappop(q)
    if c > costs[n]:
        continue
    for i in mapping[n]:
        cost = c + i[1]
        if cost < costs[i[0]]:
            costs[i[0]] = cost
            heappush(q,(cost, i[0]))

for i in range(1,v+1):
    if costs[i]==INF:
        print("INF")
    else:
        print(costs[i])