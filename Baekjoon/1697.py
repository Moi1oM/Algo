import sys


def f(num,depth):
    global k,d,checked
    print(num,depth)
    checked[num] = True
    if num == k:
        d.append(depth)
        return 0
    elif num > k:
        if not checked[num-1]:
            f(num-1, depth+1)
            return 0
    else:
        if not checked[num+1]:
            f(num+1, depth+1)
        if not checked[num-1]:
            f(num-1, depth+1)
        if not checked[num*2]:
            f(num*2, depth+1)
        return 0


n, k = map(int, sys.stdin.readline().split())
d = []
checked = [False] * (k*3)
f(n,0)
d.sort()
print(d[0])