users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
# result is [1, 5400]
import copy

answer = [0,0]

def calcu(emo, costs, users):
    don = [0] * (len(users))
    for i in range(1,len(emo)):
        for j in range(len(users)):
            if emo[i] * 10 >= users[j][0]:
                don[j] += costs[emo[i]][i-1]
    a,b = 0, 0
    for i in range(len(don)):
        if don[i]>=users[i][1]:
            a+=1
        else:
            b+=don[i]
    return a,b

def f(emo, costs, n, users):
    global answer
    n+=1
    if n == len(emo):
        a,b = calcu(emo, costs, users)
        if a>answer[0]:
            answer[0] = a
            answer[1] = b
        elif a == answer[0]:
            if b > answer[1]:
                answer[1] = b
        return
    for i in range(0,5):
        emo[n]=i
        f(emo, costs, n, users)
    return


def solution(users, emoticons):
    costs = []
    emo = [0] * (len(emoticons)+1)
    hal = 0
    while hal<0.5:
        cost = copy.deepcopy(emoticons)
        for j in range(len(cost)):
            cost[j] = cost[j] * (1-hal)
        costs.append(cost)
        hal += 0.1
    f(emo, costs, 0, users)
    return answer

print(solution(users, emoticons))