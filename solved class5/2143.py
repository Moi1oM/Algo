from sys import stdin
from collections import deque
from heapq import heappush, heappop
sin = stdin.readline

target = int(sin())
l1 = int(sin())
n1 = deque(map(int,sin().split()))
n1.appendleft(0)
l2 = int(sin())
n2 = deque(map(int,sin().split()))
n2.appendleft(0)
add1, add2 = 0, 0
nuzuk1 = []
nuzuk2 = []
for n in n1:
    add1 += n
    nuzuk1.append(add1)
for n in n2:
    add2 += n
    nuzuk2.append(add2)
q = {}
q2 = []
q2n = {}
for idx1 in range(l1+1):
    for idx2 in range(idx1+1,l1+1):
        nn = nuzuk1[idx2] - nuzuk1[idx1]
        if nn in q.keys():
            q[nn]+=1
        else:
            q[nn]=1
for idx1 in range(l2+1):
    for idx2 in range(idx1+1,l2+1):
        nn = nuzuk2[idx2] - nuzuk2[idx1]
        q2.append(nn)
        if nn in q2n.keys():
            q2n[nn] += 1
        else:
            q2n[nn] = 1
q2.sort()
def find(t):
    global q2
    s = 0
    e = len(q2) - 1
    flag = False
    while s<=e:
        mid = (s+e)//2
        if q2[mid] == t:
            flag = True
            break
        elif q2[mid] > t:
            e = mid - 1
        else: #q2[mid] < t
            s = mid + 1
    return flag
cnt = 0
for now in q.keys():
    flag = find(target-now)
    if flag:
        cnt+=q[now]*q2n[target-now]

print(cnt)