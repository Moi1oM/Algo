global d

def left():
    if d==3:
        d=0
    else:
        d+=1

N,M=map(int,input().split())
x,y,d=map(int,input().split())
land=[]
land_check=[[0]*N for _ in range(M)]
moving_x=[0,1,0,-1]
moving_y=[1,0,-1,0]
for i in range(M):
    input_list=list(map(int,input().split()))
    land.append(input_list)
land_check[x][y]=1
is_standing=0
while(True):
    left()
    is_standing+=1
    dx=x+moving_x[d]
    dy=y+moving_y[d]
    if is_standing==4:
        x=x-moving_x[d]
        y=y-moving_y[d]
        is_standing=-1
        if(d==0):
            d=3
        else:
            d-=1
        continue
    if land_check[dx][dy]==1 or land[dx][dy]==1:
        continue
    if land_check[dx][dy]==0 and land[dx][dy]==0:
        x=dx
        y=dy
        is_standing=0