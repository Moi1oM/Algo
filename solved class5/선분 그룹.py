from sys import stdin
sin = stdin.readline
n = int(sin())
dots = []
group = [[0]]

def sinbal(a,b,c):
    return (a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(a[1]*b[0]+b[1]*c[0]+c[1]*a[0])
def ccw(a,b):
    fx=a[0:2]
    fy=a[2:]
    sx=b[0:2]
    sy=b[2:]
    first=sinbal(fx,fy,sx)*sinbal(fx,fy,sy)
    second=sinbal(sx,sy,fx)*sinbal(sx,sy,fy)
    if first==0 and second==0:
        if fx>fy:
            fx,fy=fy,fx
        if sx>sy:
            sx,sy=sy,sx
        if fx<=sy and sx<=fy:
            return True
        else:
            return False
    else:
        if first<=0 and second<=0:
            return True
        else:
            return False

def is_connected(p1,p2):
    a, b, c, d = p1[0], p1[1], p1[2], p1[3]
    ap, bp, cp, dp = p2[0], p2[1], p2[2], p2[3]
    if c-a != 0:
        t_ap = (d-b)*(cp-ap)/(c-a) - (dp-bp)
        one_ap = (bp-b)-(ap-a)*(d-b)/(c-a)

        sol = one_ap / t_ap

        if sol >= 0 and sol <= 1:
            return True
        else:
            return False
    elif cp-ap != 0: # c-a == 0
        sol = (a-ap)*(dp-bp)/(cp-ap)/(d-b)

for i in range(n):
    l = list(map(int,sin().split()))
    dots.append(l)

for i in range(1,n):
    s = []
    for j in range(len(group)-1,-1,-1):
        flag = False
        for num in group[j]:
            if ccw(dots[i],dots[num]):
                flag = True
        if flag:
            s.append(j)
    if s:
        new = []
        for j in s:
            new += group[j]
            del group[j]
        new += [i]
        group.append(new)
    else:
        group.append([i])

max_len = 0
res = len(group)
for g in group:
    if len(g) > max_len:
        max_len = len(g)

print(res)
print(max_len)