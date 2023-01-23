from sys import stdin

sin = stdin.readline
INF = int(1e9)

n = int(sin())

dp = [[INF,INF] for _ in range(n+1)]
dp[n][0] = 0

if n != 1:
    for i in range(n,0,-1):
        now = dp[i][0]
        if i%3==0:
            dif = now + 1
            if dif < dp[i//3][0]:
                dp[i//3][0]=dif
                dp[i//3][1]=i
        if i%2==0:
            dif = now + 1
            if dif < dp[i//2][0]:
                dp[i//2][0]=dif
                dp[i//2][1]=i
        dif = now + 1
        if dif < dp[i-1][0]:
            dp[i-1][0]=dif
            dp[i-1][1]=i

    print(dp[1][0])

    ans = [1]
    idx = 1
    while True:
        nxt = dp[idx][1]
        ans.append(nxt)
        if nxt == n:
            break
        idx = nxt

    for index in range(dp[1][0],-1,-1):
        print(ans[index], end=" ")
else:
    print(0)
    print(1)