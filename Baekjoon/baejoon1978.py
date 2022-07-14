def f(number):
    return_val=1
    if number==1:
        return 0
    else:
        for i in range(2,number):
            if(number%i==0):
                return_val=0
                break
        return return_val

N=int(input())
count=0
d=list(map(int,input().split()))
for i in range(len(d)):
    count+=f(d[i])

print(count)