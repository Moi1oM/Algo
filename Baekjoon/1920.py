n = int(input())
d = list(map(int, input().split()))
m = int(input())
l = list(map(int, input().split()))
d.sort()

for i in l:
    check = 0
    start = 0
    end = len(d) - 1
    while True:
        mid = (start + end) // 2
        if i == d[mid]:
            check = 1
            break
        elif start >= end:
            break
        elif i < d[mid]:
            end = mid-1
        else:
            start = mid+1
    print(check)