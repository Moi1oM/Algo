from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    line =list(map(int,input().split()))
    for idx in range(1,len(line)-2,2):
        graph[line[0]].append((line[idx],line[idx+1]))
#print(graph)
def dfs(start):
    visited = [-1] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    respond = [0, start]

    while q:
        t = q.popleft()
        #print(t)
        for node, cost in graph[t]:
            #print(node)
            if visited[node] == -1:
                visited[node] = visited[t] + cost
                q.append(node)
                if visited[node] > respond[0]:
                    respond[0] = visited[node]
                    respond[1] = node
    #print(visited)

    return respond[0], respond[1]

d, m = dfs(1)
d, _ = dfs(m)
print(d)