from sys import stdin
from collections import deque
sin = stdin.readline

n = int(sin())
nums = deque(map(int, sin().split()))
nums.appendleft(0)

l = [0] * (n+1)
x = [int(1e9)] * (n+1)
x[0]=0
x_idx = 0

for i in range(1,n+1):
    for idx in range(x_idx,-1,-1):
        if x[idx] < nums[i]:
            if idx == x_idx:
                x_idx+=1
            x[idx+1] = min(x[idx+1], nums[i])
            l[i] = idx+1
            break

print(x_idx)