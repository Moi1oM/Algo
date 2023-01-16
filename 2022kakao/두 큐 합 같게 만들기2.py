from collections import deque

# queue1 = [3,2,7,2]
# queue2 = [4,6,5,1]

def solution(queue1, queue2):
    answer = -2
    d1 = deque(queue1)
    d2 = deque(queue2)
    flag = False
    l = len(queue1)
    s1 = sum(d1)
    s2 = sum(d2)
    if (s1+s2)%2!=0:
        return -1

    cnt = 0
    while s1!=s2:
        if s1>s2:
            tmp = d1.popleft()
            s1 -= tmp
            s2 += tmp
            d2.append(tmp)
        elif s1<s2:
            tmp = d2.popleft()
            s2 -= tmp
            s1 += tmp
            d1.append(tmp)
        cnt += 1
        if cnt >= l*4:
            flag = True
            break
    if flag:
        answer = -1
    else:
        answer = cnt
    return answer

print(solution(queue1,queue2))