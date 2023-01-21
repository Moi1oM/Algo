from heapq import heappush, heappop
n,m,x = map(int, input().split())
INF = int(1e9)
graph=[[] for _ in range(n+1)]
q = []
for _ in range(m):
    a, b, c =map(int, input().split())
    graph[a].append((b,c))

def dkst(start, to):
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[start] = 0
    heappush(q,(0,start))

    while q:
        now_cost, now = heappop(q)
        if now_cost > distance[now]:
            continue
        for city, city_cost in graph[now]:
            cst = now_cost + city_cost
            if distance[city] > cst:
                distance[city] = cst
                heappush(q,(cst,city))

    return distance[to]

res = 0
for i in range(1,n+1):
    s1 = dkst(i, x)
    s2 = dkst(x, i)
    if res < s1+s2:
        res = s1+s2

print(res)