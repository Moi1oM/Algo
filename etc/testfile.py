from heapq import heappush, heappop

paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]

heap = []

for p1, p2, cost in paths:
    heappush(heap, (cost, p1, p2))
    print(heap)
