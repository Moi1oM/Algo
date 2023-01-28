from sys import stdin

sin = stdin.readline

r,c = map(int,sin().split())
alphas = []
went_alpha = [False]*26
past = []
for _ in range(r):
    l = sin()
    alphas.append(l)

res = 0

def get_index(alp):
    return ord(alp)-ord('A')

def go(x,y,cnt):
    global r,c,alphas,past, res, went_alpha
    #print(x, y, cnt)
    if res < cnt:
        res = cnt
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        if px < 0 or py < 0 or px >= r or py >= c:
            continue
        idx = get_index(alphas[px][py])
        if went_alpha[idx]:
            continue
        went_alpha[idx]=True
        go(px,py,cnt+1)
        went_alpha[idx]=False

went_alpha[get_index(alphas[0][0])]=True
go(0,0,1)

print(res)

