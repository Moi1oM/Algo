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


import heapq

def solution(n, info):
    answer = [0] * 11
    q = []
    score = 10
    apch_score = 0
    for idx, apch in enumerate(info):
        if apch > 0:
            apch_score += score
        need = apch+1
        if apch == 0:
            get_score = score
        else:
            get_score = score * 2
        heapq.heappush(q,(-get_score/need ,get_score/need, need, idx, score))
        score -= 1

    lion_score = 0
    #print(lion_score, apch_score)
    while q:
        if n <= 0:
            break
        tmp = []
        flag = False
        min_score = 11
        idx = -1
        min_idx = 0
        while True:
            now = heapq.heappop(q)
            tmp.append(now)
            idx += 1
            if not q:
                break
            if q[0][1] != now[1]:
                break
            else:
                flag = True
                if min_score > now[4]:
                    min_score = now[4]
                    min_idx = idx
        if flag:
            for i, val in enumerate(tmp):
                if i == min_idx:
                    now = val
                    continue
                else:
                    heapq.heappush(q,val)

        #print(now)
        idx = now[3]
        if n >= now[2]:
            n -= now[2]
            lion_score += now[4]
            if info[idx]:
                apch_score -= now[4]
            answer[idx] += now[2]
    answer[10]+=n
    #print(lion_score, apch_score)
    if lion_score > apch_score:
        return answer
    else:
        return [-1]


print("result is",solution(n,info))