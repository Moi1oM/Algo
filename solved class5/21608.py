from sys import stdin
sin = stdin.readline

n = int(sin())

friends = [[] for _ in range((n*n)+1)]
sun = []
g = [[0]*n for _ in range(n)]

for i in range(1,(n*n)+1):
    line = list(map(int, sin().split()))
    num = line[0]
    sun.append(num)
    for i in range(1,5):
        friends[num].append(line[i])

def cal(r,c,s):
    global g,friends
    if g[r][c]!=0:
        return -1, -1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    ret = 0
    ret2 = 0
    for i in range(4):
        px = r + dx[i]
        py = c + dy[i]
        if px < 0 or py < 0 or px>=n or py>=n:
            continue
        if g[px][py] in friends[s]:
            ret+=1
        if g[px][py]==0:
            ret2+=1
    return ret, ret2

def cal2(r,c,s):
    global g,friends
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    ret = 0
    for i in range(4):
        px = r + dx[i]
        py = c + dy[i]
        if px < 0 or py < 0 or px>=n or py>=n:
            continue
        if g[px][py] in friends[s]:
            ret+=1
    return ret

for st in sun:
    max_cnt, max_cnt2 = -1, -1
    g_cnt = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            cnt, cnt2 = cal(r,c,st)
            g_cnt[r][c] = (cnt, cnt2)
            if max_cnt < cnt:
                max_cnt = cnt
    c1, c2 = 0, 0
    d1 = []
    d2 = []
    for r in range(n):
        for c in range(n):
            if g_cnt[r][c][0] == max_cnt:
                c1 += 1
                d1.append((r,c))
    for r,c in d1:
        if max_cnt2 < g_cnt[r][c][1]:
            max_cnt2 = g_cnt[r][c][1]
    for r,c in d1:
        if g_cnt[r][c][1] == max_cnt2:
            c2 += 1
            d2.append((r,c))

    if c1 == 1:
        g[d1[0][0]][d1[0][1]]=st
    else:
        g[d2[0][0]][d2[0][1]]=st

    # for r in range(n):
    #     for c in range(n):
    #         print(g[r][c], end=" ")
    #     print()
    # print()

result = 0
for r in range(n):
    for c in range(n):
        r1 = cal2(r,c,g[r][c])
        # print(r1)
        if r1 == 0:
            continue
        else:
            result += 10**(r1-1)

print(result)