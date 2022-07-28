import sys
n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
d.sort(reverse = True)
sum = 0
for i in range(n):
    sum+=d[i]*(i+1)
print(sum)