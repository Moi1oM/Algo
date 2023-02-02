from sys import stdin

sin = stdin.readline

n = int(sin())
nums = list(map(int, sin().split()))
for _ in range(n-1):
    a, b, c = map(int, sin().split())
