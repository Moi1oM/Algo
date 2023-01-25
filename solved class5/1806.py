from sys import stdin
from collections import deque
sin = stdin.readline

n ,m = map(int, sin().split())
nums = deque(map(int, sin().split()))
nums.appendleft(0)

s_n = []
cnt = 0
for n in nums:
    cnt += n
    s_n.append(cnt)

i1, i2 = 0, 1
res = int(1e9)
while i1 <= i2 and i2 < len(s_n):
    now = s_n[i2] - s_n[i1]
    if now >= m:
        if i2-i1 < res:
            res = i2-i1
        i1 += 1
    else:
        i2 += 1
if res == int(1e9):
    print(0)
else:
    print(res)