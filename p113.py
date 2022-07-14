N=int(input())
count=0
ccount=0
def f(hour):
    val=0
    if(hour<10):
        if(hour==3):
            val=1
    else:
        if(hour%10==3):
            val=1
        hour=hour//10
        if(hour==3):
            val=1
    return val

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            check1=0
            check2=0
            ii=f(i)
            ij=f(j)
            ik=f(k)
            if '3' in str(i)+str(j)+str(k):
                ccount+=1
                check1=1
            if(ii==1 or ij==1 or ik==1):
                count+=1
                check2=1
            if check1!=check2:
                print(i,j,k,ik)

print(count,ccount)