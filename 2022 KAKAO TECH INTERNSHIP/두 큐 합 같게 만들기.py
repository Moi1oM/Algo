queue1 = [1,2,1,2]
queue2 = [1,10,1,2]

def cal_queue(i1, i2, tQ):
    l = len(tQ)
    if l//2 <= i1:
        if i2 == l-1:
            return i1 - l//2
        else:
            return i2 - l//2 +1 +i1
    else:
        return i1 + i2 - l//2 +1

def solution(queue1, queue2):
    answer = int(1e9)
    total_sum = sum(queue1)+sum(queue2)
    if total_sum % 2 != 0:
        return -1
    goal = total_sum // 2
    totalQueue = queue1 + queue2
    write_all = []
    for l in range(1,len(totalQueue)+1):
        f_idx = 0
        s_idx = f_idx + l - 1
        s = sum(totalQueue[f_idx:s_idx+1])
        while True:
            if s==goal:
                write_all.append((f_idx,s_idx))
            s-=totalQueue[f_idx]
            f_idx+=1
            s_idx+=1
            if s_idx == len(totalQueue):
                break
            s+=totalQueue[s_idx]
    if not write_all:
        return -1
    for can in write_all:
        idx1 = can[0]
        idx2 = can[1]
        tmp = cal_queue(idx1,idx2, totalQueue)
        if tmp<answer:
            answer = tmp
    return answer

print(solution(queue1, queue2))