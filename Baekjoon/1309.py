n=int(input())
a=1
b=1
c=1
if n == 1 :
    print(3)
else:
    for i in range(2,n+1):
        na=a+b+c
        nb=a+c
        nc=a+b
        a=na
        b=nb
        c=nc
    print((na+nb+nc)%9901)