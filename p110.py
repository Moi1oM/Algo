N=int(input())
x=1
y=1
d=list(input().split())
xx=1
yy=1
for i in range(len(d)):
    if(d[i]=='L'):
        xx=x-1
    if(d[i]=='R'):
        xx=x+1
    if(d[i]=='U'):
        yy=y-1
    if(d[i]=='D'):
        yy=y+1
    if(xx<1 or xx>N or yy<1 or yy>N):
        continue
    else:
        x=xx
        y=yy
print(x,y)
