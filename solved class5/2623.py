from collections import deque
from sys import stdin

sin = stdin.readline

n, m = map(int, sin().split())
in_degree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    line = list(map(int,sin().split()))
    for idx, val in enumerate(line):
        if idx >= 2 :
            in_degree[val] += 1
            graph[line[idx-1]].append(val)
def go():
   result = []
   q = deque()
   for i in range(1, n+1):
       if in_degree[i] == 0:
           q.append(i)
   while q:
       now = q.popleft()
       result.append(now)
       for i in graph[now]:
           in_degree[i]-=1
           if in_degree[i]==0:
               q.append(i)

   if len(result) == n:
       for v in result:
           print(v)
   else:
       print(0)
go()
