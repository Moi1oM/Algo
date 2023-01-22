n = int(input())
waters = list(map(int, input().split()))
waters.sort()

def solve():
    if waters[0] >= 0:
        print(waters[0],waters[1],waters[2])
        return
    if waters[-1] <= 0:
        print(waters[-3],waters[-2],waters[-1])
        return
    res = int(1e10)
    r1, r2, r3 = 0, 0, 0
    for i in range(n-2):
        target, s, e = waters[i], i+1, n-1
        while s<e:
            now = target + waters[s] + waters[e]
            if abs(now) < res:
                res = abs(now)
                r1, r2, r3 = target, waters[s], waters[e]
            if abs(now) == 0:
                break
            elif now < 0:
                s += 1
            elif now > 0:
                e -= 1
        if now == 0:
            break

    print(r1,r2,r3)
    return
solve()