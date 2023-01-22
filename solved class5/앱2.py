INF = int(1e10)
n, m = map(int, input().split())
using = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [[0]*(10001) for _ in range(n+1)]

for i in range(1,n+1):
    get, c = using[i-1], costs[i-1]
    for j in range(10001):
        if j<c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j-c]+get, dp[i-1][j])

# for i in range(n+1):
#     for j in range(101):
#         print((j,dp[i][j]), end=" ")
#     print()


for i, val in enumerate(dp[n]):
    if val >= m:
        print(i)
        break