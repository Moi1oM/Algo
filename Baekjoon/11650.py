import sys
n=int(sys.stdin.readline())
d=[]
for _ in range(n):
    a,b=map(int, sys.stdin.readline().split())
    d.append((a,b))
d.sort()
for i in d:
    print(i[0],i[1])