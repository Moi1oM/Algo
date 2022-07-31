import sys
input=sys.stdin.readline

N, M=map(int, input().split())
a=list(map(int, input().split()))
smallest=300000
from itertools import combinations
for i in combinations(a, 3):
#    print(sum(i))

    if M-sum(i)<0:
        cha=3000000
    else:
        cha=M-sum(i)
        if cha<smallest:
            smallest=cha
            fin=sum(i)
            print("changing", smallest, fin)
print(fin)