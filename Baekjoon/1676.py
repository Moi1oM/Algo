import sys

n = int(sys.stdin.readline())
a = 0
b = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        num = i
        while num % 2 == 0:
            a += 1
            num //= 2
    if i % 5 == 0:
        num = i
        while num % 5 == 0:
            b += 1
            num //= 5
print(min(a, b))
