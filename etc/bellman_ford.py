import sys
input = sys.stdin.readline
INF = int(1e9)
n ,m = map(int, input().split())
distance = [INF]*(n+1)
costs = []

for i in range(m):
    a, b, c =map(int, input().split())
    costs.append((a,b,c))

def bellman_ford(start):
    distance[start]=0
    res = False
    for i in range(n):
        for j in range(m):
            now = costs[j][0]
            to = costs[j][1]
            cost = costs[j][2]
            if distance[now]!=INF and distance[to] > distance[now]+cost:
                distance[to]= distance[now]+cost
                if i==n-1:
                    res=True
    return res


doIt = bellman_ford(1)

if doIt:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i]==INF:
            print(-1)
        else:
            print(distance[i])