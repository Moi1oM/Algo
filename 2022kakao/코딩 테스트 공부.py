alp = 0
cop = 0
#problems = [[10,15,2,1,2],[20,20,3,3,4]]
problems = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]


# answer is 15

def solution(alp, cop, problems):
    answer = 0
    possible = []
    goal_alp = 0
    goal_cop = 0
    for p in problems:
        if p[0] > goal_alp:
            goal_alp = p[0]
        if p[1] > goal_cop:
            goal_cop = p[1]
    dp = [[int(1e9)] * (goal_cop + 1) for _ in range(goal_alp + 1)]
    dp[alp][cop]=0
    goal_alp = max(goal_alp, alp)
    goal_cop = max(goal_cop, cop)
    for i in range(alp,goal_alp+1):
        for j in range(cop, goal_cop+1):
            if i < goal_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < goal_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for p in problems:
                if i>=p[0] and j>=p[1]:
                    new_alp = min(i+p[2], goal_alp)
                    new_cop = min(j+p[3], goal_cop)
                    dp[new_alp][new_cop]=min(dp[new_alp][new_cop], dp[i][j]+p[4])

    # for i in range(goal_alp + 1):
    #     for j in range(goal_cop + 1):
    #         t1 = i - alp
    #         if t1 < 0:
    #             t1 = 0
    #         t2 = j - cop
    #         if t2 < 0:
    #             t2 = 0
    #         dp[i][j] = t1 + t2
    # for p in problems:
    #     for i in range(goal_alp + 1):
    #         for j in range(goal_cop + 1):
    #             if i >= p[0] and j >= p[1]:
    #                 pi = i + p[2]
    #                 pj = j + p[3]
    #                 if pi > goal_alp or pj > goal_cop:
    #                     continue
    #                 dp[pi][pj] = min(dp[pi][pj], dp[i][j] + p[4])

    # for i in range(goal_alp+1):
    #     for j in range(goal_cop+1):
    #         print(dp[i][j], end=" ")
    #     print()
    answer = dp[goal_alp][goal_cop]
    return answer


print(solution(alp, cop, problems))
