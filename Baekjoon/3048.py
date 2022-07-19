n1,n2=map(int,input().split())
group1=input()
group2=input()
t=int(input())
group11=group1[::-1]
minlen=min(n1,n2)
d=[]
for i in range(n1):
    d.append((group11[i],0))
for i in range(n2):
    d.append((group2[i],1))
time=0
#print(d)
while time<t:
#    print("time: ",time,d)
    index=0
    while True:
 #       print("index: ",index," d: ",d)
        if d[index][1]==0 and d[index+1][1]==1:
            d[index], d[index+1]= d[index+1], d[index]
            # d[index][0],d[index+1][0]=d[index+1][0],d[index][0]
            # d[index][1],d[index+1][1]=d[index+1][1],d[index][1]
            index+=2
        else:
            index+=1
        if index>=(n1+n2-1):
            break
    time+=1
for i in range(n1+n2):
    print(d[i][0],end="")