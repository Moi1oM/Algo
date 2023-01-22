from itertools import product
import copy
room_first = []

def f(idx_i, idx_j):
    global room
    dx = [0,0,0,-1,1]
    dy = [0,-1,1,0,0]
    for i in range(5):
        px = idx_i + dx[i]
        py = idx_j + dy[i]
        if px < 0 or py < 0 or px >= 10 or py >= 10:
            continue
        room[px][py] = not room[px][py]

for _ in range(10):
    line = input()
    l = []
    for i in line:
        if i=='#':
            l.append(False)
        if i=='O':
            l.append(True)
    room_first.append(l)

res = int(1e9)
for x in product(range(2),repeat=10):
    cnt = 0
    room = copy.deepcopy(room_first)
    cnt += sum(x)
    #print(cnt)
    for i in range(10):
        if x[i] == 1:
            f(0,i)
    for i in range(1,10):
        for j in range(10):
            if room[i-1][j]:
                #print((i,j), end=" ")
                cnt+=1
                f(i,j)
    flag = True
    for i in range(10):
        if room[9][i]:
            flag = False
            break
    if flag:
        if cnt < res:
            res = cnt
    # flag = 1
    # for i in range(10):
    #     if room[0][i] % 2 != 0:
    #         flag = 0
    #         break
    #
    # if flag:
    #     print(room_first[0])
    #     print(room[0])
    #     print(x)

if res != int(1e9):
    print(res)
else:
    print(-1)