n, m = map(int, input().split())
mapping = [[-1]*101 for _ in range(101)]


def f(n,r):
    if mapping[n][r]!=-1:
        return mapping[n][r]
    if n==r or r==0:
        mapping[n][r]=1
        return 1
    else:
        mapping[n][r]=f(n-1,r-1)+f(n-1,r)
        return mapping[n][r]

print(f(n,m))