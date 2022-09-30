n = int(input())
nums = list(map(int,input().split()))
res = [1]*n

for i in range(1, n):
    max_num = 0
    for j in range(i-1,-1,-1):
        if nums[j]<nums[i] and max_num < res[j]:
            max_num = res[j]
    res[i] = max_num + 1

print(max(res))