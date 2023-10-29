import sys
input = sys.stdin.readline
print = sys.stdout.write


n = int(input())

matrix = []
nums = []
dp = [[987654321] * (n+1) for _ in range(n+1)]

for i in range(n):
    m, nn = map(int, input().split())
    if i == 0:
        nums.append(m)
    nums.append(nn)
    matrix.append([m, nn])

for x in range(1, n+1):
    dp[x][x] = 0

for i in range(1, n):
    for j in range(1, n-i+1):
        temp_min = 987654321
        for k in range(i):
            temp = dp[j][j+k] + dp[j+k+1][j+i] + nums[j-1] * nums[j+k] * nums[j+i]
            temp_min = min(temp_min, temp)
        dp[j][j+i] = temp_min

print(str(dp[1][n]))