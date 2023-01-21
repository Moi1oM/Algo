n, m = map(int, input().split())
INF = int(1e9)
res = INF

def f(num, cnt):
    global res
    if num == m:
        if cnt < res:
            res = cnt
        return
    elif num > m:
        return
    else:
        f(num*2, cnt+1)
        f(num*10+1, cnt+1)

f(n,1)

if res==INF:
    print(-1)
else:
    print(res)