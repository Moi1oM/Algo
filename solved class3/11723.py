import sys

n = int(sys.stdin.readline().rstrip())

s = set()

for _ in range(n):
    line = sys.stdin.readline().rstrip().split()
    if len(line) == 1:
        if line[0] == 'empty':
            s = set()
        if line[0] == 'all':
            s = set([i for i in range(1, 21)])
    if len(line) == 2:
        op, num = line[0], int(line[1])
        if op == 'add':
            s.add(num)
        if op == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        if op == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        if op == 'remove':
            if num in s:
                s.remove(num)