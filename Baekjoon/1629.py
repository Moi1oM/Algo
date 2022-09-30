import sys

#d = [0]* 2147483648
d=[]
def cnum(num,n):
    if d[n]!=0:
        return d[n]
    else:
        if n==1:
            d[n]=num
            return num
        else:
            x = cnum(num, n//2)
            if n % 2 == 0:
                d[n]=x*x
                return d[n]
            else:
                d[n]=x*x*num
                return d[n]


def fpow(C, n):
    res = 1
    while n:
        print(C,n,res)
        if n != 1:
            res *= C
        C *= C
        n //= 2

    return res

a, b, c = map(int, sys.stdin.readline().split())

#print(cnum(a,b)%c)
print(fpow(a,b)%c)