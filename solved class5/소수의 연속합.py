from sys import stdin
from collections import deque
import math
sin = stdin.readline

n = int(sin())
sosu = [True]*(n+1)
sosu[0], sosu[1] = False, False
MAX = 4000000

d = deque()

for i in range(2,int(math.sqrt(n))+1):
    for j in range(2*i, n+1, i):
        sosu[j] = False

s = 0
d.append(s)
for i in range(2,n+1):
    if sosu[i]:
        s += i
        d.append(s)

idx1 = 0
idx2 = 0
cnt = 0
while idx1<=idx2 and idx2 < len(d):
    now = d[idx2] - d[idx1]
    if now == n:
        cnt+=1
        idx2+=1
    elif now < n:
        idx2 += 1
    else: # now > n
        idx1 += 1

print(cnt)