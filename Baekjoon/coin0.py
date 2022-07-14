N,K=map(int,input().split())
d=[]
for _ in range(N):
    a=int(input())
    d.append(a)
d.reverse()
index=0
count=0
while(K!=0):
    if(K<d[index]):
        index+=1
        continue
    cc=K//d[index]
    K=K-cc*d[index]
    count+=cc
print(count)