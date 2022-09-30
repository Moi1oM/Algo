import sys
n = int(sys.stdin.readline().rstrip())
d = [0] * 1001
maxday = 0
work = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if maxday < a:
        maxday = a
    work.append((b,a))
work.sort(reverse=True)
for i in range(n):
    for j in range(work[i][1],0,-1):
        if d[j]<work[i][0]:
            d[j]=work[i][0]
            break
res = 0
for i in range(1,maxday+1):
    res+=d[i]
print(res)