N,M=map(int,input().split())
d=[]
for i in range(N):
    d.append(list(map(int,input())))

def dfs(x,y):
    if(x<=-1 or x>=N or y<=-1 or y>=M):
        return False
    if d[x][y]==0:
        d[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
res=0
for i in range(N):
    for j in range(M):
        if(dfs(i,j)==True):
            res+=1
print(res)