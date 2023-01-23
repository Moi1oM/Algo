from sys import stdin
from copy import deepcopy
sin = stdin.readline


n = int(sin())

def f(n):
    ex_nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    now_nums = [0] * 10

    dx = [-1, 1]
    for _ in range(n-1):
        for i in range(10):
            for k in dx:
                idx = i+k
                if idx<0 or idx>=10:
                    continue
                now_nums[idx]+=ex_nums[i]

        ex_nums = deepcopy(now_nums)
        now_nums = [0] * 10
    print(n,ex_nums)
    return sum(ex_nums)

#print(f(n))
cnt = 0
for i in range(1,41):
    r = f(i)
    cnt += r%1000000000
print(cnt)
#print(sum(ex_nums)%1000000000)