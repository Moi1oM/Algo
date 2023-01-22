from heapq import heappush, heappop
import copy

INF = int(1e10)
n, m = map(int, input().split())
using = list(map(int, input().split()))
costs = list(map(int, input().split()))
q = []
ex_dp = [INF] * (m+1)
now_dp = [INF] * (m+1)
#dp = [[INF]*(m+1) for _ in range(n+1)]
# for i in range(m+1):
#     dp[0][i] = INF
# for i in range(n+1):
#     dp[i][0] = 0
ex_dp[0]=0
now_dp[0]=0

for i in range(1,n+1):
    get, c =using[i-1], costs[i-1]
    for j in range(m+1):
        if ex_dp[j] == INF:
            continue
        for k in range(get+1):
            if j+k > m:
                break
            now_dp[j+k] = min(ex_dp[j+k], ex_dp[j]+c, now_dp[j+k])
    ex_dp = copy.deepcopy(now_dp)
    now_dp = [INF] * (m+1)
    now_dp[0] = 0
# for i in range(n+1):
#     for j in range(m+1):
#         print((j,dp[i][j]), end = " ")
#     print()
# print()

print(ex_dp[m])