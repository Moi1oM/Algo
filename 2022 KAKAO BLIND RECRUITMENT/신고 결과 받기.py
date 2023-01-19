#id_list = ["muzi", "frodo", "apeach", "neo"]
id_list = ["con", "ryan"]
#report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

def solution(id_list, report, k):
    answer = [0]*len(id_list)

    unq = set()

    for rpt in report:
        unq.add(rpt)

    con = {}

    for one in unq:
        frm, to = one.split()
        if to in con.keys():
            con[to]+=1
        else:
            con[to]=1

    for one in unq:
        frm, to = one.split()
        if con[to] >= k:
            answer[id_list.index(frm)] += 1

    return answer

print("answer is",solution(id_list, report, k))