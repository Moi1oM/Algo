import sys
n = int(sys.stdin.readline())
mapping = []
white = 0
blue = 0

def f(a,b,c,d):
    global mapping, white, blue
    color = mapping[a][b]
    check = True
    for i in range(a,c):
        for j in range(b,d):
            if mapping[i][j] != color:
                check = False
                break
    if not check:
        mid1 = (a+c)//2 #6
        mid2 = (b+d)//2 #2
        f(a,b,mid1,mid2)
        f(a,mid2,mid1,d)
        f(mid1,b,c,mid2)
        f(mid1,mid2,c,d)
    else:
        if color == 1:
            blue += 1
        if color == 0:
            white += 1
        return 0

for _ in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    mapping.append(a)
f(0,0,n,n)

print(white)
print(blue)