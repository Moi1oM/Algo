a,b=map(int,input().split())
A=max(a,b)
B=min(a,b)
for i in range(A,0,-1):
    if A % i == 0 and B % i == 0:
        minnum = i
        break
print(minnum)
print(a*b//minnum)