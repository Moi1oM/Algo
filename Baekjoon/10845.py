from collections import deque
import sys
que = deque()
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    do = sys.stdin.readline().rstrip()
    if do[0] == 'p' and do[1] == 'u':
        trash, num = do.split()
        que.append(int(num))
    if do[0] == 'p' and do[1] == 'o':
        if len(que)==0:
            print(-1)
        else:
            print(que.popleft())
    if do[0] == 's':
        print(len(que))
    if do[0] == 'e':
        if len(que)==0:
            print(1)
        else:
            print(0)
    if do[0] == 'f':
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
    if do[0] == 'b':
        if len(que)==0:
            print(-1)
        else:
            print(que[len(que)-1])