import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
que = PriorityQueue()

for _ in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if que.qsize() != 0:
            print(que.get())
        else:
            print(0)
    else:
        que.put(a)