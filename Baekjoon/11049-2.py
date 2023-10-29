n = int(input())
nums = []
dp = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(n):
    r, c = map(int, input().split())
    if i == 0:
        nums.append(r)
    nums.append(c)

for x in range(1, n+1):
    dp[x][x] = 0

for l in range(1, n):
    for i in range(1, n-l+1):
        j = i + l
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j]
            dp[i][j] = min(dp[i][j], cost)

print(dp[1][n])
