import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
d = []
for i in range(1,n+1):
    d.append(i)
for i in combinations(d,m):
    for j in range(len(i)):
        print(i[j], end=" ")
    print()