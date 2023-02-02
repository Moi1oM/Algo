from sys import stdin
from collections import deque
sin = stdin.readline

n=int(sin())
nums = deque(map(int,sin().rstrip().split()))
nums.appendleft(0)
m=int(sin())
dp = [[False]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][i]=True
    if i==n:
        continue
    if nums[i] == nums[i+1]:
        dp[i][i+1]=True

for i in range(n-1,0,-1):
    for j in range(i+2,n+1):
        if nums[i]==nums[j] and dp[i+1][j-1]:
            dp[i][j]=True

for _ in range(m):
    a, b = map(int, sin().split())
    if dp[a][b]:
        print(1)
    else:
        print(0)