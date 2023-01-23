from sys import stdin
sin = stdin.readline
from heapq import heappush,heappop, heapify

n,m,k = map(int, sin().rstrip().split())
cards = list(map(int, sin().rstrip().split()))
heapify(cards)
reds = list(map(int, sin().rstrip().split()))

for red in reds:
    q = []
    while True:
        now = heappop(cards)
        if now > red:
            print(now)
            break
        else:
            heappush(q,now)

    while q:
        n = heappop(q)
        heappush(cards,n)
