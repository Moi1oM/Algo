from sys import stdin
sin = stdin.readline

n = int(sin())
nums = list(map(int, sin().split()))

def binary_search(s, e, t):
    global seq
    ret = 10000000
    while s<=e:
        mid = (s+e)//2
        if seq[mid] >= t:
            if ret > mid:
                ret = mid
            e = mid - 1
        else: #arr[mid] < t
            s = mid + 1
    seq[ret] = t

seq = [nums[0]]
idx = 0
for i in range(1,n):
    num = nums[i]
    if seq[idx]<num:
        seq.append(num)
        idx+=1
    else:
        binary_search(0,idx,num)

print(len(seq))