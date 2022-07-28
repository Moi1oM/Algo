import sys

n = int(sys.stdin.readline())
paper = []
res = [0, 0, 0]


def f(si1, ei1, si2, ei2):
    global paper, res
    check = False
    a = paper[si1][si2]
    for i in range(si1, ei1):
        for j in range(si2, ei2):
            if a != paper[i][j]:
                check = True
                break
    if check:

        it1 = ei1 - si1
        it2 = ei2 - si2
        it1 //= 3
        it2 //= 3

        for i in range(si1, ei1, it1):
            for j in range(si2, ei2, it2):
                f(i, i + it1, j, j + it2)
    else:
        if a == -1:
            res[0] += 1
        elif a == 0:
            res[1] += 1
        elif a == 1:
            res[2] += 1


for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

f(0, n, 0, n)
for i in res:
    print(i)