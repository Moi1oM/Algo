from sys import stdin
sin = stdin.readline

n, k = map(int, sin().split())
b = []
bags = []

for _ in range(n):
    w, c =map(int, sin().split())
    b.append((c,w))
b.sort(reverse=True)
for _ in range(k):
    w = int(sin())
    bags.append(w)
bags.sort()
is_max_used = False
parent = [i for i in range(k)]

def find_p(x):
    global parent
    if parent[x]==x:
        return x
    else:
        parent[x]=find_p(parent[x])
        return parent[x]

def union_p(a,b):
    if b>=k:
        return
    global parent
    aa = find_p(a)
    bb = find_p(b)
    if aa>bb:
        parent[bb]=aa
    else:
        parent[aa]=bb

def bin_search(target):
    s = 0
    e = k-1
    idx = k-1
    if target > bags[idx]:
        return -1
    while s<=e:
        mid = (s+e)//2
        if bags[mid]>=target:
            if bags[mid] < bags[idx]:
                idx = mid
            e = mid - 1
        else:
            s = mid + 1
    return idx

def is_it_possible(w):
    i = bin_search(weight)
    if i == -1:
        return False, -1
    ind = find_p(i)
    return True, ind

cnt = 0
used = [0]*k

for cost, weight in b:
    flag, index = is_it_possible(weight)
    if flag:
        if is_max_used and index == k-1:
            continue
        elif index == k-1 and not is_max_used:
            is_max_used = True
        cnt+=cost
        union_p(index,index+1)
        used[index] = 1

print(cnt)