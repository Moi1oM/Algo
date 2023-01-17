n=5
paths = [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
gates = [1,2 ]
summits = [5]
#result is [5, 3]
from heapq import heappush, heappop

ans_path = []

def find_parent(x, parent):
    global ans_path
    ans_path.append(x)
    if parent[x] != x:
        return find_parent(parent[x], parent)
    return x

def union_parent(nod1, nod2, parent):
    a = find_parent(nod1, parent)
    b = find_parent(nod2, parent)
    if a < b:
        parent[nod2] = nod1
    elif a > b:
        parent[nod1] = nod2

def is_connected(g,s,parent):
    if find_parent(g, parent) == find_parent(s, parent):
        return True
    else:
        return False

def solution(n, paths, gates, summits):
    global ans_path
    answer = []
    max_cost = 0
    hiking = [[] for _ in range(n+1)]
    mapping = [[False]*(n+1) for _ in range(n+1)]
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i]=i

    heap = []
    for p1, p2, cost in paths:
        if cost > max_cost:
            max_cost = cost
        heappush(heap, (cost, p1, p2))
    flag = False
    while True:
        for l in range(1,max_cost+1):
            while heap and heap[0][0] == l:
                cost, p1, p2 = heappop(heap)
                mapping[p1][p2] = True
                mapping[p2][p1] = True
                union_parent(p1,p2, parent)
            for gate in gates:
                for summit in summits:
                    ans_path = []
                    flag = is_connected(gate, summit, parent)
                    if flag:
                        for n in ans_path:
                            if n in summits:
                                answer.append(n)
                                break
                        answer.append(l)
                        break
                if flag:
                    break
            if flag:
                break
        if flag:
            break

    return answer

print("answer is ",solution(n, paths, gates, summits))