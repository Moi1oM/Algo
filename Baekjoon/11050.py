import sys
n, k = map(int, sys.stdin.readline().split())

def f(n, k):
    if n==k or k==0:
        return 1
    else:
        return f(n-1,k-1)+f(n-1,k)

print(f(n, k))