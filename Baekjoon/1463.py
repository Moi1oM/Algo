import sys
n = int(sys.stdin.readline())
d=[987654321]*(3*n+1)
d[1] = 0
for i in range(1,n):
    d[i+1]=min(d[i]+1, d[i+1])
    d[i*2]=min(d[i]+1, d[i*2])
    d[i*3]=min(d[i]+1, d[i*3])
print(d[n])