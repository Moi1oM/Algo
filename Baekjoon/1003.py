import sys
n=int(sys.stdin.readline())
# def fibo(n):
#     if fibonum[n] != -1 :
#         return fibonum[n]
#     else:
#         return fibo(n-1)+fibo(n-2)
fibonum=[-1]*(41)
fibonum[0]=0
fibonum[1]=1
for i in range(2,41):
    fibonum[i]=fibonum[i-1]+fibonum[i-2]

for _ in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        print(1,0)
    else:
        print(fibonum[a-1],fibonum[a])