n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
# result is [0,2,2,0,1,0,0,0,0,0,0]
#n = 1
#info = [1,0,0,0,0,0,0,0,0,0,0]
#result is [-1]
#n = 9
#info = [0,0,1,2,0,1,1,1,1,1,1]
#result is [1,1,2,0,1,2,2,0,0,0,0]
#n = 10
#info = [0,0,0,0,0,0,0,0,3,4,3]
# result is [1,1,1,1,1,1,1,1,0,0,2]

from itertools import combinations_with_replacement as combi
from collections import Counter

# for i in combi(range(11),5):
#     cnt = Counter(i)
#     print(cnt)
answer = [0]*11
max_point = 0

def cal(n, info):
    global answer, max_point
    for ss in combi(range(11),n):
        cnt = Counter(ss)
        lion_score, apch_score = 0, 0
        for i in range(11):
            if cnt[i] > info[10-i]:
                lion_score += i
            elif info[10-i]:
                apch_score += i
        if lion_score - apch_score > max_point:
            max_point = lion_score - apch_score
            for i in range(11):
                answer[10-i] = cnt[i]

def solution(n, info):
    global answer, max_point
    cal(n,info)
    if max_point == 0:
        answer = [-1]
    return answer

print("answer is",solution(n,info))