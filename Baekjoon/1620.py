import sys

d = {}
dd = {}
n, m = map(int, sys.stdin.readline().split())
for i in range(1, n+1):
    a = input()
    d[str(i)] = a
    dd[a] = str(i)


for i in range(m):
    a = input()
    if not a.isdigit():
        print(dd[a])
    else:
        print(d[a])