n = int(input())
INF = int(1e9)
#graph = [[INF]*(n+1) for _ in range(n+1)]
graph = [[]]
for i in range(1,n+1):
    l = [INF] * (i+1)
    graph.append(l)

def print_all(g, n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(g[i][j], end = " ")
        print()
    print()

for i in range(1,n+1):
    line = list(map(int, input().split()))
    idx = 1
    while idx + 1 < len(line):
        if line[0]>=line[idx]:
            graph[line[0]][line[idx]]=line[idx+1]
        idx+=2

for i in range(1,n+1):
    graph[i][i]=0

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if b>a:
                a1 = b
                b1 = a
            else:
                a1 = a
                b1 = b
            if k>a:
                a2 = k
                k2 = a
            else:
                a2 = a
                k2 = k
            if b>k:
                k3 = b
                b3 = k
            else:
                k3 = k
                b3 = b
            # if a==b or grap
            # h[a][k]==0 or graph[k][b]==0:
            #     continue
            graph[a1][b1] = min(graph[a1][b1],graph[a2][k2]+graph[k3][b3])
            # print(k,a,b)
            # print_all(graph, n)

res = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        if i==j:
            continue
        if res < graph[i][j]:
            res = graph[i][j]

print(res)