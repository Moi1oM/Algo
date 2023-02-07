from sys import stdin
sin = stdin.readline
INF = int(1e9)
nums = list(map(int,sin().split()))
costs = [[0,2,2,2,2],[INF,1,3,4,3],[INF,3,1,3,4],[INF,4,3,1,3],[INF,3,4,3,1]]
nums.pop()
le = len(nums)
if le == 0:
    print(0)
    exit()
dp = [[[INF]*(5) for _ in range(5)] for _ in range(le+1)]
dp[-1][0][0]=0

for i in range(le):
    #왼발이 nums[i]로 움직인다.
    for r in range(5):
        for k in range(5):
            him = costs[k][nums[i]]
            dp[i][nums[i]][r] = min(dp[i][nums[i]][r], dp[i-1][k][r]+him)

    #오른발이 nums[i]로 움직인다.
    for l in range(5):
        for k in range(5):
            him = costs[k][nums[i]]
            dp[i][l][nums[i]]=min(dp[i][l][nums[i]],dp[i-1][l][k]+him)

res = INF

for i in range(5):
    for j in range(5):
        res = min(res, dp[le-1][i][j])
print(res)
# for i in range(l):
#     for j in range(5):
#         for k in range(5):
#             print(dp[i][j][k], end=" ")
#         print()
#     print()
#     print()