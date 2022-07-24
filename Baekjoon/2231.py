n=int(input())

def f(num):
    cnt=num
    while num>0:
        cnt+=num%10
        num=num//10
    return cnt

for i in range(1,n+1):
    a=f(i)
    if a==n:
        print(i)
        break
    if i==n:
        print(0)