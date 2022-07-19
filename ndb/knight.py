def f(x,y):
    if x>0 and y>0 and x<=8 and y<=8:
        return 1
    else:
        return 0
a=input()
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]
chan = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
x=chan[a[0]]
y=int(a[1])
count=0
for i in range(8):
    px=x+dx[i]
    py=y+dy[i]
    count+=f(px,py)
print(count)