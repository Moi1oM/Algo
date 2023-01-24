from sys import stdin

sin = stdin.readline

n = int(sin())
waters = list(map(int,sin().split()))

def bin_s(target):
    global answer
    s = 0
    e = n-1
    while s<=e:
        mid = (s+e)//2
        if waters[mid] == target and target!=0:
            answer = [-target, target]
            break
        elif waters[mid] > target:
            if abs(waters[mid] - target) < abs(sum(answer)) and target+waters[mid]!=0:
                answer = [-target, waters[mid]]
                if answer[0] > answer[1]:
                    answer[1], answer[0] = answer[0], answer[1]
            e = mid - 1
        else: # waters[mid] < target
            if abs(waters[mid] - target) < abs(sum(answer)) and target+waters[mid]!=0:
                answer = [-target, waters[mid]]
                if answer[0] > answer[1]:
                    answer[1], answer[0] = answer[0], answer[1]
            s = mid + 1

if waters[0] >= 0:
    print(waters[0], waters[1])
elif waters[-1] <= 0:
    print(waters[-2], waters[-1])
else:
    INF = int(1e10)
    answer = [INF, INF]
    for i in range(n-1):
        s = waters[i]
        target = -s
        bin_s(target)

print(answer[0],answer[1])