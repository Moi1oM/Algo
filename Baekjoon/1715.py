from queue import PriorityQueue
import sys
que = PriorityQueue()
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    que.put(a)
sum = 0
while True:
    if que.qsize()==1:
        break
    else:
        a=que.get()
        b=que.get()
        sum += (a+b)
        que.put(a+b)
print(sum)