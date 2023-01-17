n = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def next_city(x, y):
    global souver, souver_nums
    if len(souver) > souver_nums[x][y]:
        souver_nums[x][y] = len(souver)
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        if px < 0 or py < 0 or px >= r or py >= c:
            continue
        if city[px][py] in souver:
            continue
        souver.append(city[px][py])
        next_city(px, py)
        souver.pop()


for i in range(n):
    city = []
    r, c = map(int, input().split())
    souver_nums = [[0]*c for _ in range(r)]
    for _ in range(r):
        line = input()
        city.append(line)
    souver = []
    souver.append(city[0][0])
    souver_nums[0][0] = 1
    x, y = 0, 0
    next_city(x,y)
    res = 0
    for a in range(r):
        for b in range(c):
            if res < souver_nums[a][b]:
                res = souver_nums[a][b]
    print(f"#{i+1}", res)