from sys import stdin
from heapq import heappush, heappop
sin = stdin.readline

n, k = map(int, sin().split())
b = []
bags = []

for _ in range(n):
    w, c =map(int, sin().split())
    heappush(b,(w,c))
for _ in range(k):
    w = int(sin())
    bags.append(w)
bags.sort()
candidate = []
cnt = 0
for bag in bags:
    while b and bag >= b[0][0]:
        weight, cost = heappop(b)
        heappush(candidate, -cost)
    #print(bag,candidate)
    if candidate:
        cnt -= heappop(candidate)

print(cnt)