from sys import stdin
sin = stdin.readline

n,m,k = map(int, sin().rstrip().split())
cards = sorted(map(int, sin().rstrip().split()))
reds = list(map(int, sin().rstrip().split()))
parent = [i for i in range(m+1)]

def union_p(idx1,idx2):
    if idx2 >= m:
        return
    global parent
    a = print_p(idx1)
    b = print_p(idx2)
    parent[a]=b


def print_p(x):
    global parent
    if parent[x] == x:
        return x
    else:
        parent[x] = print_p(parent[x])
        return parent[x]

def binary_search(red):
    global cards
    s, e = 0, m-1
    upper = int(1e9)
    idx = -1
    while s<=e:
        mid = (s+e)//2
        if cards[mid]> red:
            if cards[mid] < upper:
                upper = cards[mid]
                idx = mid
            e = mid -1
        else: #cards[mid] < red
            s = mid + 1

    return idx

for red in reds:
    index = binary_search(red)
    i = print_p(index)
    print(cards[i])
    # print(index, u, val, idx)
    # print()
    union_p(i, i+1)