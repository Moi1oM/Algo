import sys
n = int(sys.stdin.readline())
d = []
res = []
for _ in range(n):
    d.append(int(sys.stdin.readline()))
    res.append((0,0))
res[0]=(d[0],1)

for i in range(1,n):
    if i == 1:
        a = d[0]